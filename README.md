# scraping-soup

## Installation

Clone repository
```
git clone https://github.com/Grister/scraping-soup.git
```

Create and activate virtual environment
```
cd scraping-soup
python3 -m venv venv
source venv/bin/activate
```

Install dependencies
```
pip3 install -r requirements.txt 
```

### Run application

Install migrations
```
python3 manage.py migrate
```
Run server
```
python3 manage.py runserver
```
