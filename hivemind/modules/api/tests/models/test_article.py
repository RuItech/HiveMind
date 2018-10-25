"""
Tests for API Module Signals
"""

from django.test import TestCase

from model_mommy import mommy


class TestArticle(TestCase):
    """
    Test for Article Model
    """

    def test_article_str_representation(self):
        """
        Expects that the headline is returned.
        """

        article = mommy.make(
            'api.Article',
            headline='Test headline',
            content='Test content.'
        )

        self.assertEqual(str(article), 'Test headline')
