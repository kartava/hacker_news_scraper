
Hacker_News_Scraper
========================

Below you will find basic setup and deployment instructions for the hacker_news_scraper
project. To begin you should have the following applications installed on your
local development system:

- Python >= 2.7
- NodeJS >= 4.2
- npm >= 2.14.7
- `pip <http://www.pip-installer.org/>`_ >= 1.5
- `virtualenv <http://www.virtualenv.org/>`_ >= 1.10
- `virtualenvwrapper <http://pypi.python.org/pypi/virtualenvwrapper>`_ >= 3.0
- Postgres >= 9.3
- git >= 1.7

A note on NodeJS 4.2 for Ubuntu users: this LTS release may not be available through the
Ubuntu repository, but you can configure a PPA from which it may be installed::

    curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
    sudo apt-get install -y nodejs

You may also follow the manual instructions if you wish to configure the PPA yourself:

    https://github.com/nodesource/distributions#manual-installation

Django version
------------------------

The Django version configured in this template is conservative. If you want to
use a newer version, edit ``requirements/base.txt``.

Getting Started
------------------------

First clone the repository from Github and switch to the new directory::

    $ git clone git@github.com:kartava/hacker_news_scraper.git
    $ cd hacker_news_scraper

To setup your local environment you should create a virtualenv and install the
necessary requirements::

    # Check that you have python2.7 installed
    $ which python2.7
    $ mkvirtualenv hacker_news_scraper -p `which python2.7`
    (hacker_news_scraper)$ pip install -r requirements/dev.txt
    (hacker_news_scraper)$ npm install

Next, we'll set up our local environment variables. We use `django-dotenv
<https://github.com/jpadilla/django-dotenv>`_ to help with this. It reads environment variables
located in a file name ``.env`` in the top level directory of the project. The only variable we need
to start is ``DJANGO_SETTINGS_MODULE``::

    (hacker_news_scraper)$ cp hacker_news_scraper/settings/local.example.py hacker_news_scraper/settings/local.py
    (hacker_news_scraper)$ echo "DJANGO_SETTINGS_MODULE=hacker_news_scraper.settings.local" > .env

Create the Postgres database and run the initial migrate::

    (hacker_news_scraper)$ createdb -E UTF-8 hacker_news_scraper
    (hacker_news_scraper)$ python manage.py migrate


Development
-----------

You should be able to run the development server::

    (hacker_news_scraper)$ python manage.py runserver

Or, on a custom port and address::

    (hacker_news_scraper)$ python manage.py runserver 0.0.0.0:8080

Any changes made to Python, files will be detected and rebuilt transparently as
long as the development server is running.


Testing
-------

For run API tests follow the command::

    (hacker_news_scraper)$ python manage.py test

For run Spider tests follow::

    cd scraper/
    (hacker_news_scraper/scraper)$ python -m unittest discover
    
    
Parsing
-------

For start parsing follow the command::

    cd scraper/
    (hacker_news_scraper/scraper)$ scrapy crawl news -a page_count=N
where, N is the number of pages you need to parse

