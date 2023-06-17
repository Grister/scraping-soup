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

### Endpoints that work

* /tasks/: The main page of the site.
* /about/: Provides information about the system, describing the functionality of the site.
* /: Same as /tasks/, as a shortcut to the main page.
* /<uuid:uuid>/: View details of a single task.
* /<uuid:uuid>/update/: The page for updating a task.
* /<uuid:uuid>/delete/: The task deletion page.
* /sign-up/: The user registration page.
* /sign-in/: The user login page.
* /logout/: The user's logout page.
