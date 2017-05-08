# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from hacker_news_scraper.posts.models import Post


class PostViewSetTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        posts = []

        for i in xrange(5):
            posts.append(Post(title='Cool title {}'.format(i),
                              author='Some author ... {}'.format(i),
                              url='https://google.com/news?p={}'.format(i),
                              site='https://google.com/news?p={}'.format(i),
                              )
                         )

        Post.objects.bulk_create(posts)

    def _check_status_code(self, response, status_code):
        self.assertEqual(response.status_code, status_code)

    def test_post_list_view(self):
        response = self.client.get(reverse('api:post-list'))
        self._check_status_code(response, 200)
        post_id_list = Post.objects.values_list('id', flat=True)
        results_post_id_list = [post['id'] for post in response.data['results']]
        self.assertListEqual(sorted(post_id_list), sorted(results_post_id_list))

    def test_post_detail_view(self):
        post = Post.objects.first()
        view_url = reverse('api:post-detail', args=[post.id])
        response = self.client.get(view_url)
        self._check_status_code(response, 200)
        self.assertEqual(post.id, response.data['id'])

    def test_allowed_methods(self):
        view_url = reverse('api:post-list')
        response_post = self.client.post(view_url)
        self._check_status_code(response_post, 405)
        response_put = self.client.post(view_url)
        self._check_status_code(response_put, 405)
        response_delete = self.client.post(view_url)
        self._check_status_code(response_delete, 405)
