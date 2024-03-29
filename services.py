import pandas as pd
import requests
from bs4 import BeautifulSoup
from config.settings import BASE_DIR


class MostPopularTVShows:

    url = "https://www.imdb.com/chart/tvmeter"

    def get_tv_shows(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")

        poster_tags = soup.find_all('td', class_="posterColumn")
        title_tags = soup.find_all('td', class_="titleColumn")
        rating_tags = soup.find_all('td', class_="ratingColumn imdbRating")

        assert len(poster_tags) == len(title_tags) == len(rating_tags) == 100, "Error occurred while scrapping "

        results = []
        for i in range(len(poster_tags)):
            poster_image = self.parse_poster_image(tag=poster_tags[i])
            title = self.parse_title(tag=title_tags[i])
            year = self.parse_year(tag=title_tags[i])
            rating = self.parse_rating(tag=rating_tags[i])

            results.append(
                {
                    'poster_image': poster_image,
                    'title': title,
                    'year': year,
                    'rating': rating
                }
            )
        return results

    def parse_poster_image(self, tag):
        return tag.find('img')['src']

    def parse_title(self, tag):
        return tag.find('a').text

    def parse_year(self, tag):
        return int(tag.find('span').text.lstrip('(').rstrip(')').strip())

    def parse_rating(self, tag):
        try:
            return float(tag.find('strong').text.strip())
        except AttributeError:
            return 0


if __name__ == '__main__':
    service = MostPopularTVShows()
    shows = service.get_tv_shows()

    df = pd.DataFrame.from_dict(shows)

    output_file_path = BASE_DIR / 'TVShows.csv'
    df.to_csv(output_file_path)
