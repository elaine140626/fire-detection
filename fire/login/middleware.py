from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
import json

class LoginFilter(MiddlewareMixin):

    white_list = ['/login/']
    def process_request(self, request):
        next_url = request.path_info
        if next_url in self.white_list or request.session.get('is_login') :
            return
        else:
            ret = {
                "code": 10001,
                "msg": "not login"
            }
            return redirect('/login/')
