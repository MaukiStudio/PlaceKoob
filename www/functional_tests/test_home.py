#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from time import sleep

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class HomeTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = WebDriver()
        cls.browser.implicitly_wait(5)
        super(HomeTest, cls).setUpClass()
        
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(HomeTest, cls).tearDownClass()

    def test_can_connect_home(self):
        # 홈페이지에 접속을 한다.
        self.browser.get(self.live_server_url)

        # 타이틀에 PlaceKoob 이 있는 것을 확인한다
        self.assertIn('PlaceKoob', self.browser.title)
        
        # 회원가입 링크를 발견하고 클릭하면 회원가입폼으로 연결됨을 확인한다
        self.assertTrue(False, 'ing...')