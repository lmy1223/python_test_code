# -*- coding: utf-8 -*-

import requests

class HttpStatusUtil:

    def __init__(self, http_url):
        self.http_url = http_url

    def get_http_status_response(self):
        req = requests.get(url=self.http_url)

        status_code = req.status_code
        status_information = req.reason

        response = {
            "status_code": status_code,
            "status_information": status_information
        }

        return response
