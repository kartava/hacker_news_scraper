from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from hacker_news_scraper.api import views
from hacker_news_scraper.api.posts_views import PostViewSet

router = SimpleRouter()
router.register(r'posts', PostViewSet, base_name='post')

urlpatterns = [
    url(r'^$', views.api_tree),
    url(r'^', include(router.urls)),
]
