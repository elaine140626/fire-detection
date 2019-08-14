from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
import login.status_code as code
import json


class LoginFilter(MiddlewareMixin):
    api_prefix = '/api/'
    login_api = '/api/user/login/'

    def process_request(self, request):
        next_url = request.path_info
        print(next_url[0: len(self.api_prefix)])
        if next_url[0: len(self.api_prefix)] == self.api_prefix:
            print(next_url[0: len(self.login_api)])
            print(next_url)
            if next_url[0: len(self.login_api)] == self.login_api:
                return
            if request.session.get('is_login'):
                return
            else:
                ret = {
                    "code": code.LOGIN_FILTER_NOT_LOGIN,
                    "msg": "not login"
                }
                return HttpResponse(json.dumps(ret))
        else:
            return
