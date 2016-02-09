#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.test import TestCase


class HomeConnectTest(TestCase):

    def setUp(self):
        super(HomeConnectTest, self).setUp()
        self.response = self.client.get('/')

    def tearDown(self):
        super(HomeConnectTest, self).tearDown()
        
    def test_status_200(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_uses_template(self):
        self.assertTemplateUsed(self.response, 'home.html')