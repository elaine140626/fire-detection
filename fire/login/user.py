import login.models as models
from login import session
import json
from django.http import HttpResponse
from django.core.handlers import wsgi


def check_is_login_and_get_username(request):
    response = HttpResponse()
    if session.check_is_login(request):
        response.status_code = 200
        response.content = request.session['name']
    else:
        response.status_code = 400
        response.content = 'Not login'
    return response


def login(request: wsgi.WSGIRequest):
    response = HttpResponse()

    if session.check_is_login(request):
        response.status_code = 200
        response.content = '已登录'

    if request.method == "POST":
        print(request.body)
        data = json.loads(request.body)
        user_name = data.get('username')
        password = data.get('password')
        # user_name = request.GET.get('param')
        # password  = request.GET.get('password')

        try:
            user = get_user_by_user_name(user_name)
            if user.password == password:
                session.set_session(request, True, user.name, user.id)
                response.status_code = 200
                response.content = "欢迎你\n" + user.name
            else:
                response.status_code = 400
                response.content = '用户名或密码不正确'
        except models.User.DoesNotExist:
            response.status_code = 400
            response.content = 'User not exists'

    else:
        response.status_code = 400
        response.content = "Wrong method"

    return response


def get_user_by_user_name(user_name: str) -> models.User:
    return models.User.objects.get(name=user_name)
