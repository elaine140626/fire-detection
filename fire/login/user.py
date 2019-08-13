import login.models as models
from login import session
import json
from django.http import HttpResponse


def check_is_login_and_get_username(request):
    response = HttpResponse()
    if session.check_is_login(request):
        response.status_code = 200
        response.content = request.session['name']
    else:
        response.status_code = 400
        response.content = 'Not login'
    return response


def new_login(request):
    response = HttpResponse()

    if session.check_is_login(request):
        response.status_code = 200
        response.content = '已登录'

    if request.method == "POST":
        data = json.loads(request.body)
        params = data.get('params')
        user_name = params.get('username')
        password = params.get('password')
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
        except "User not exists":
            response.status_code = 400
            response.content = 'User not exists'

    else:
        response.status_code = 400
        response.content = "Wrong method"

    return response


def get_user_by_user_name(user_name: str) -> models.User:
    if not models.User.objects.filter(name=user_name).exists():
        raise Exception("User not exists", user_name)

    return models.User.objects.get(name=user_name)
