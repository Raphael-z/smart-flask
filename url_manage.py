#coding:utf8

from TEST.url import app_url as test_app_url
from TEST.url import api_url as test_api_url


class UrlManage(object):

    @classmethod
    def register_app_url(self,app):
        """
        注册app url
        :param app:
        :return:
        """
        test_app_url(app)

    @classmethod
    def register_api_url(self,api):
        """
        注册api url
        :param app:
        :return:
        """
        test_api_url(api)

