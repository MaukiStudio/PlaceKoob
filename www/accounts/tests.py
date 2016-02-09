#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.test import TestCase
from django.core.urlresolvers import reverse


class AccountsConnectTest(TestCase):

    def setUp(self):
        super(AccountsConnectTest, self).setUp()
        self.response = self.client.get(reverse('accounts'))

    def tearDown(self):
        super(AccountsConnectTest, self).tearDown()
        
    def test_status_200(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_uses_template(self):
        self.assertTemplateUsed(self.response, 'accounts.html')