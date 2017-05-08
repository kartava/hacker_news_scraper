import sys
import os
import django


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(BASE_DIR, os.pardir))
os.environ['DJANGO_SETTINGS_MODULE'] = 'hacker_news_scraper.settings.local'
django.setup()
