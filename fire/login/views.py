from django.shortcuts import render
from . import models
from .forms import UserForm
from django.core import serializers
from django.http import HttpResponse
import requests
import time
import json
import datetime

# Create your views here.

from django.shortcuts import render, redirect

URL = "http://140.143.244.242:8080/weixin/wxsend/sendTemp"


def warning(request):
    ret_vars = {}

    if request.session.get('is_login', None):
        ret_vars['username'] = request.session['user_name']

        user = models.User.objects.get(name=request.session['user_name'])
        user_message = models.User_Message.objects.values('message_id', 'true_or_false').filter(user_id=user.id)
        print(user_message)
        user_message_dict = {}
        for i in user_message:
            print(i)
            user_message_dict[i['message_id']] = 'true'
        print(user_message_dict)
        message_list = models.Message.objects.all()

        user_message_list = [{
            'id': i.id,
            'content': i.content,
            'img_url': i.img_url,
            'device_number': i.serial_number.id,
            'device_hint': i.serial_number.hint,
            'deal': i.id in user_message_dict,
            'c_time': i.c_time.strftime('%Y-%m-%d')
        }
            for i in message_list]

        print(user_message_list)
        ret_vars['user_message_list'] = json.dumps(user_message_list)

        # ret_vars['message_list'] = serializers.serialize('json', message_list)

        return render(request, 'warning.html', ret_vars)

    return redirect('/login')


def overview(request):
    ret_vars = {}

    if request.session.get('is_login', None):
        ret_vars['username'] = request.session['user_name']

        user = models.User.objects.get(name=request.session['user_name'])
        user_message = models.User_Message.objects.values('message_id').filter(user_id=user.id)
        user_message_list = [i['message_id'] for i in user_message]
        message_list = models.Message.objects.exclude(id__in=user_message_list)
        message_count = models.Message.objects.count()
        device_count = models.Device.objects.count()
        devices = models.Device.objects.all()
        device_points = []
        for d in devices:
            device_points.append([d.location_x, d.location_y, d.video_url, d.hint])

        ret_vars['message_list'] = serializers.serialize('json', message_list)
        ret_vars['device_count'] = device_count
        ret_vars['un_deal'] = message_count - len(user_message)
        ret_vars['user_deal'] = len(user_message)
        ret_vars['device_points'] = json.dumps(device_points)
        print(user_message)

        return render(request, 'overview.html', ret_vars)

    return redirect('/login')


def monitor(request):
    ret_vars = {}

    if request.session.get('is_login', None):
        ret_vars['username'] = request.session['user_name']
        user = models.User.objects.get(name=request.session['user_name'])
        video_list = models.Video.objects.filter(user_id=user.id)
        ret_vars['video_list'] = serializers.serialize('json', video_list)
        ret_vars['default_layout'] = user.layout

        return render(request, 'monitor.html', ret_vars)

    return redirect('/login')


def login(request):
    ret_var = {}
    login_form = UserForm(request.POST)
    ret_var['login_form'] = login_form

    if request.session.get('is_login', None):
        return redirect('/overview')

    if request.method == "POST":

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            username = username.strip()
            print(username)
            print(password)

            # print("I'm hhhhhhhherre")
            try:
                # print("I'm hhhhhhhherre")
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/overview/')
                else:
                    ret_var['message'] = '密码不正确'
            except:
                print("I got some problems")
                return render(request, 'login.html', ret_var)

    return render(request, 'login.html', ret_var)


def empty_redirect(request):
    return redirect('/overview/')


def logout(request):
    # the logout function

    if not request.session.get('is_login', None):
        return redirect('/login/')

    request.session.flush()

    return redirect('/login/')


def DealData(request):
    if request.method == "POST":

        data = request.POST.get('data')
        data = json.loads(data)
        print(type(data.get('code')))
        if data.get('code', None) == 0:
            data = data.get('data')
            print(data)
            for dd in data:
                print(dd.get('camera_id'))
                try:
                    device = models.Device.objects.get(serial_number=dd.get('camera_id'))
                    models.Message.objects.create(content='来自设备id为 ' + dd.get('camera_id', None) + ' 的报警信息',
                                                  img_url=dd.get('image_url', None), serial_number=device)
                except:
                    raise Exception()
                else:
                    tmp_data = {
                        "title": "你有新的预警消息！",
                        "warnContent": "您的设备" + dd.get('camera_id') + '发出了一条报警信息',
                        "warnTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                        "remarks": models.Device.objects.get(serial_number=dd.get('camera_id')).hint,
                        "warnUrl": "http://188.131.241.21/warning/",
                    }
                    result = requests.post(URL, tmp_data)
                    print(result.content)

        return HttpResponse('oddk')

    else:
        return HttpResponse('emm')


def dealTrue(request):
    response = HttpResponse()

    if not request.session.get('is_login', None):
        response.status_code = 400
        response.content = '没有登陆'
        return response

    if request.method == 'POST':

        id_array = request.POST['data'].split(',')

        print(id_array)
        user = models.User.objects.get(name=request.session['user_name'])

        try:
            for id in id_array:
                message = models.Message.objects.get(id=id)
                if models.User_Message.objects.filter(user_id=user, message_id=message).exists():
                    models.User_Message.objects.filter(user_id=user, message_id=message).update(true_or_false=True)
                else:
                    models.User_Message.objects.create(user_id=user, message_id=models.Message.objects.get(id=id),
                                                       true_or_false=True)
        except:
            response.status_code = 500
            raise Exception()

        else:
            response.status_code = 200

        return response

    else:

        response.status_code = 404
        response.content = '找不到页面'
        return response


def dealFalse(request):
    response = HttpResponse()

    if not request.session.get('is_login', None):
        response.status_code = 400
        response.content = '没有登陆'
        return response

    if request.method == 'POST':

        id_array = request.POST['data'].split(',')

        print(id_array)
        user = models.User.objects.get(name=request.session['user_name'])

        try:

            for id in id_array:
                message = models.Message.objects.get(id=id)
                if models.User_Message.objects.filter(user_id=user, message_id=message).exists():
                    models.User_Message.objects.filter(user_id=user, message_id=message).update(true_or_false=False)
                else:
                    models.User_Message.objects.create(user_id=user, message_id=models.Message.objects.get(id=id),
                                                       true_or_false=False)
        except:
            response.status_code = 500
            raise Exception()

        else:
            response.status_code = 200

        return response

    else:

        response.status_code = 404
        response.content = '找不到页面'
        return response


def MessageAmount(request):
    response = HttpResponse()

    if not request.session.get('is_login', None):
        response.status_code = 400
        response.content = '没有登陆'
        return response

    response.content = models.Message.objects.all().count()
    print(response.content)
    response.status_code = 200
    return response


def conf(request):
    ret_vars = {}

    if request.session.get('is_login', None):
        ret_vars['username'] = request.session['user_name']

        return render(request, 'conf.html', ret_vars)

    return redirect('/login')
