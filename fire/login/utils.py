import json
from django.http import HttpResponse


def serve_data_response(response: HttpResponse, data):
    response.status_code = 200
    response.content = json.dumps({
        "code": 0,
        "msg": "",
        "data": data
    })


def serve_error_response(response: HttpResponse, code: int, msg: str):
    response.status_code = 200
    response.content = json.dumps({
        "code": code,
        "msg": msg
    })