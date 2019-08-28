from login import models, status_code, session, utils
from login import user as User
from django.core.handlers import wsgi
from django.http import HttpResponse
import json


def videos_controller(request: wsgi.WSGIRequest):
    response = HttpResponse()

    if request.method == 'GET':
        user_name = session.get_user_name(request)
        user = User.get_user_by_user_name(user_name)
        videos = models.Video.objects.filter(user_id=user.id)
        ret = []
        for video in videos:
            ret.append(convert_video_model_to_dict(video))
        utils.serve_data_response(response, ret)
    elif request.method == 'POST':
        data = json.loads(request.body)
        if not isinstance(data, dict):
            response.status_code = 400
            response.content = 'wrong parameters: check the data'
        else:
            video_id = data.get('video_id')
            video_url = data.get('video_url')
            if video_id is None or video_url is None:
                utils.serve_400_response('wrong parameters: check the video_id and the video_url cannot be empty')
            else:
                models.Video.objects.filter(id=video_id).update(video_url=video_url)
            utils.serve_data_response(response, '')
    return response


def convert_video_model_to_dict(video: models.Video) -> dict:
    return {
        "id": video.id,
        "video_url": video.video_url
    }
