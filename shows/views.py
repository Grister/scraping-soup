from django.shortcuts import render
from services import MostPopularTVShows
from shows.models import TVShow


def index(request):

    service = MostPopularTVShows()
    top_movies = service.get_tv_shows()

    for top_show in top_movies:
        show = (
            TVShow.objects
            .filter(
                title=top_show.get('title'),
                year=top_show.get('year')
            )
            .first()
        )
        if show:
            show.poster_image = top_show.get('poster_image')
            show.rating = top_show.get('rating')
            show.save()
        else:
            show = TVShow(
                poster_image=top_show.get('poster_image'),
                title=top_show.get('title'),
                year=top_show.get('year'),
                rating=top_show.get('rating'),
            )
            show.save()

    return render(request, 'shows/index.html')


def shows(request):
    shows = TVShow.objects.all()

    context = {
        'shows': shows
    }
    return render(request, template_name='shows/tvshows.html', context=context)
