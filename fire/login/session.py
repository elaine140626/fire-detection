import django.core.handlers.wsgi as wsgi


def check_is_login(request: wsgi.WSGIRequest):
    # return the status of login
    return request.session.get('is_login', None)


def get_user_name(r):
    return r.session.get('user_name')


def flush_session(request):
    request.session.flush()


def set_session(request: wsgi.WSGIRequest, is_login: bool, user_name: str, user_id: int):
    request.session['is_login'] = is_login
    request.session['user_name'] = user_name
    request.session['user_id'] = user_id
