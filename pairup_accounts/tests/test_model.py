import pytest
from django.test import TestCase
from django.conf import settings
from pairup_accounts.models import MyAccountManager
from django.contrib.auth import get_user_model
# Create your tests here.

class SettingsTest(TestCase):    
    def test_account_is_configured(self):
        assert 'accounts' in INSTALLED_APPS
        assert 'accounts.User' == AUTH_USER_MODEL

def test_new_user(django_user_model):
    django_user_model.objects.create(username="someone", password="something")

@pytest.mark.django_db
def test_user_count():
    assert User.objects.count() == 0

import unittest


class Tests(unittest.TestCase):

    def setUp(self):
        print('setUp')

    def test_skip(self):
        print('skip')
        self.skipTest('skip')

    def tearDown(self):
        print('tearDown')
        
        
        



    