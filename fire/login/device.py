from login import models, utils, status_code
from django.core.handlers import wsgi
from django.http import HttpResponse


def device_controller(request: wsgi.WSGIRequest):
    response = HttpResponse()
    if request.method == "GET":
        device_id = request.GET.get("device_id")
        if device_id is None:
            response.status_code = 400
            response.content = "parameters device_id is None"
        else:
            device = get_device_by_id(device_id)
            ret = convert_models_device_to_dict(device)
            utils.serve_data_response(response, ret)
    else:
        response.status_code = 400
        response.content = "wrong request method"
    return response


def get_all_device_controller(request: wsgi.WSGIRequest):
    response = HttpResponse()

    if request.method == 'GET':
        devices = all_devices()
        ret = []
        for d in devices:
            ret.append(convert_models_device_to_dict(d))
        utils.serve_data_response(ret)
    else:
        response.status_code = 400
        response.content = "wrong request method"
    return response


def convert_models_device_to_dict(device: models.Device) -> dict:
    return {
        "id": device.id,
        "serial_number": device.serial_number,
        "location_x": device.location_x,
        "location_y": device.location_y,
        "hint": device.hint,
        "video_url": device.video_url
    }


def all_devices() -> []:
    return models.Device.objects.all()


def get_device_by_id(device_id: int) -> models.Device:
    return models.Device.objects.get(id=device_id)
