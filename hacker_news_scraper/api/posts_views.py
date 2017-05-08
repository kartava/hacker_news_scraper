# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from hacker_news_scraper.api.posts_serializers import PostListSerializer, \
    PostDetailSerializer
from hacker_news_scraper.posts.models import Post


class PostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def retrieve(self, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super(PostViewSet, self).retrieve(*args, **kwargs)
