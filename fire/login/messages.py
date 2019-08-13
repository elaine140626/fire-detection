from login import session, models
from login import user as User
from django.core.handlers import wsgi
from django.http import HttpResponse
import json


def messages(request: wsgi.WSGIRequest):
    response = HttpResponse()
    if request.method == "GET":
        user_name = session.get_user_name(request)
        offset = request.GET.get('offset', 0)
        limit = request.GET.get('limit', - 1)
        type = request.GET.get('type', 'all')
        # todo 高层的封装
        if type == 'all':
            response.content = json.dumps(get_all_messages(limit,offset))
        elif type == 'unread':
            response.content = json.dumps(get_messages_unread_by_user_name(user_name, limit, offset))
        else:
            response


    elif request.method == "POST":
        data = json.loads(request.body)
        params = data.get('params')


def get_all_messages(limit=-1, offset=0) -> []:
    if limit == -1:
        return models.Message.objects.all()[offset:]
    else:
        return models.Message.objects.all()[offset:offset + limit]


def get_messages_unread_by_user_name(user_name: str, limit: int = - 1, offset: int = 0) -> []:
    # return the message unread by the user
    user = User.get_user_by_user_name(user_name)
    user_message = models.User_Message.objects.values('message_id').filter(user_id=user.id)
    user_message_list = [i['message_id'] for i in user_message]
    if limit == -1:
        return models.Message.objects.exclude(id__in=user_message_list)[offset:]
    else:
        return models.Message.objects.exclude(id__in=user_message_list)[offset:offset + limit]
