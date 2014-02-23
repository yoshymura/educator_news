from django.test import TestCase
from django.core.urlresolvers import reverse

from ed_news.views import invalidate_cache


class EdNewsViewTests(TestCase):

    def test_index_cache(self):
        """Request index, then invalidate cache.
        Cache should be invalidated, returning True.
        Then try to invalidate, and should return False.
        """
        response = self.client.get(reverse('ed_news:index'))
        self.assertEqual(response.status_code, 200)

        invalidated = invalidate_cache('index', namespace='ed_news')
        self.assertEqual(invalidated, True)

        invalidated = invalidate_cache('index', namespace='ed_news')
        self.assertEqual(invalidated, False)        
