#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: Common.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 2月 24, 2020
# ---


# 定义一个common的类，它的父类是object
# just testdemo
import requests


# 定义一个common的类，它的父类是object
class Common(object):
    # common的构造函数
    def __init__(self,url_root):
        # 被测系统的跟路由
        self.url_root = url_root
    # 封装get请求，uri是访问路由，params是get请求的参数，如果没有默认为空
    def get(self, uri, params=''):
        # 拼凑访问地址
        url = self.url_root + uri + params
        # 通过get请求访问对应地址
        res = requests.get(url)
        # 返回request的Response结果，类型为requests的Response类型
        return res
    # 封装post方法，uri是访问路由，params是post请求需要传递的参数，如果没有参数这里为空
    def post(self, uri, params=''):
        # 拼凑访问地址
        url = self.url_root + uri
        if len(params) > 0:
            # 如果有参数，那么通过post方式访问对应的url，并将参数赋值给requests.post默认参数data
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.post(url, data=params)
        else:
            # 如果无参数，访问方式如下
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.post(url)
            return res


    def put(self,uri,params=None):
        '''
        封装put方法，uri是访问路由，params是put请求需要传递的参数，如果没有参数这里为空
        :param uri: 访问路由
        :param params: 传递参数，string类型，默认为None
        :return: 此次访问的response
        '''
        url = self.url_root+uri
        if params is not None:
            # 如果有参数，那么通过put方式访问对应的url，并将参数赋值给requests.put默认参数data
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.put(url, data=params)
        else:
            # 如果无参数，访问方式如下
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.put(url)

        return res


    def delete(self,uri,params=None):
        '''
        封装delete方法，uri是访问路由，params是delete请求需要传递的参数，如果没有参数这里为空
        :param uri: 访问路由
        :param params: 传递参数，string类型，默认为None
        :return: 此次访问的response
        '''
        url = self.url_root + uri
        if params is not None:
            # 如果有参数，那么通过delete方式访问对应的url，并将参数赋值给requests.delete默认参数data
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.delete(url, data=params)
        else:
            # 如果无参数，访问方式如下
            # 返回request的Response结果，类型为requests的Response类型
            res = requests.delete(url)
        return res