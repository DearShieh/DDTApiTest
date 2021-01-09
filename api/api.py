"""
    @file: api.py
    @Author: Shieh
    @Date: 2021/1/2 23:30
    @Description: 
"""

import requests
from config import host


class Api:
    def __init__(self, case):
        self.url = host + case.get("path")
        self.method = case.get("method")
        self.param_type = case.get("param_type")
        self.headers = case.get("headers")
        self.params = case.get("params")

    def __get(self):
        return requests.get(url=self.url, params=self.params, headers=self.headers)

    def __post(self):
        if self.param_type == "json":
            return requests.post(url=self.url, json=self.params, headers=self.headers)
        elif self.param_type == "date":
            return requests.post(url=self.url, data=self.params, headers=self.headers)

    def __put(self):
        return requests.put(url=self.url, data=self.params, headers=self.headers)

    def __delete(self):
        return requests.delete(url=self.url, params=self.params, headers=self.headers)

    def run_method(self):
        if self.method == "get":
            return self.__get()
        elif self.method == "post":
            return self.__post()
        elif self.method == "put":
            return self.__put()
        elif self.method == "delete":
            return self.__delete()
        else:
            print("ERROR Method.")
