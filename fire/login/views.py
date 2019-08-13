from . import models
from .forms import UserForm
from django.core import serializers
from django.http import HttpResponse
import requests
import time
import json
import hashlib
import login.wechat_receive as receive
import login.reply as reply
from login import session

# Create your views here.

from django.shortcuts import render, redirect

URL = "http://140.143.244.242:8080/weixin/wxsend/sendTemp"


def warning(request):
    print("This is the type")
    print(type(request))
    ret_vars = {}

    if session.check_is_login(request):
        user_name = session.get_user_name(request)
        ret_vars['username'] = user_name

        user = models.User.objects.get(name=user_name)
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

    if session.check_is_login(request):
        user_name = session.get_user_name(request)
        ret_vars['username'] = user_name

        user = models.User.objects.get(name=user_name)
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

    if session.check_is_login(request):
        user_name = session.get_user_name(request)
        ret_vars['username'] = user_name
        user = models.User.objects.get(name=user_name)
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

    if not session.check_is_login(request):
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
                    img_url = dd.get('image_url')
                    serial_number = device.serial_number
                    warning_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    warning_message = "您在经度为 " + str(device.location_x) + " 纬度为 " + str(
                        device.location_y) + "的设备发出了一条报警信息"
                    hint = device.hint
                    reply.WarningMessageToAll(img_url, serial_number, warning_date, warning_message, hint)
                    print(result.content)

        return HttpResponse('oddk')

    else:
        return HttpResponse('emm')


def dealTrue(request):
    response = HttpResponse()

    if not session.check_is_login(request):
        response.status_code = 400
        response.content = '没有登陆'
        return response

    if request.method == 'POST':

        id_array = request.POST['data'].split(',')

        print(id_array)
        user = models.User.objects.get(name=session.get_user_name(request))

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

    if not session.check_is_login(request):
        response.status_code = 400
        response.content = '没有登陆'
        return response

    if request.method == 'POST':

        id_array = request.POST['data'].split(',')

        print(id_array)
        user = models.User.objects.get(name=session.get_user_name(request))

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

    if not session.check_is_login(request):
        response.status_code = 400
        response.content = '没有登陆'
        return response

    response.content = models.Message.objects.all().count()
    print(response.content)
    response.status_code = 200
    return response


def conf(request):
    ret_vars = {}

    if session.check_is_login(request):
        ret_vars['username'] = request.session['user_name']

        return render(request, 'conf.html', ret_vars)

    return redirect('/login')


def wechat(request):
    if request.method == "GET":

        signature = request.GET.get("signature")
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        token = "1122345"

        print(signature, timestamp, nonce, echostr)

        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1((''.join(list)).encode('utf-8'))
        map(sha1.update, list)
        hashcode = sha1.hexdigest()

        print(hashcode, signature, )
        if hashcode == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("")
    elif request.method == "POST":
        ct = request.body
        content = ct.decode()
        recMsg = receive.parse_xml(content)

        ret = ""
        print(type(recMsg))

        if isinstance(recMsg, receive.ClickEventMsg):
            ret = reply.DealWithEventMsg(recMsg).send()
            print(ret)
            return HttpResponse(ret)
        elif isinstance(recMsg, receive.SubScribeEventMsg):
            reply.UserAdded(recMsg)
            print("This is the subscribeEventmsg")
            wechat_user = models.WechatUser.objects.all()
            for i in wechat_user:
                print(i.open_id)
                ret = reply.TextMsg(recMsg.FromUserName, recMsg.ToUserName, "感谢关注公众号。我们将及时为您推送报警信息").send()
                print(ret)
                return HttpResponse(ret)
        elif isinstance(recMsg, receive.UnsubscribeEventMsg):
            pass
        elif isinstance(recMsg, receive.TextMsg):
            ret = reply.DealWithTextMsg(recMsg).send()
            return HttpResponse(ret)

        print(ct)
        print(content)
        return HttpResponse(ret)

    return HttpResponse("213244")


def getUserConf(request):
    response = HttpResponse()

    if not session.check_is_login(request):
        response.status_code = 400
        response.content = '没有登陆'
        return response

    if request.method == "GET":

        user_name = request.session["user_name"]
        user = models.User.objects.get(name=user_name)

        response.content = json.dumps({
            "layout": user.layout,
            "email": user.email,
            "wechatOpenId": user.wechat_id,
            "telephone": user.phone
        })
        response.status_code = 200

    else:
        response.status_code = 400
        response.content = "Wrong Method"

    return response


def get_messages(request):
    response = HttpResponse()

    if not session.check_is_login(request):
        response.status_code = 400
        response.content = 'Not Login'
        return response

    if request.method == "GET":
        limit = generate_parameter(request, "limit")
        offset = generate_parameter(request, "offset")
        type = generate_parameter(requests, "type")
        limit = int(limit)
        offset = int(offset)

        if type == "unread":
            pass

        user_name = get_user_name(request)

        print(user_name)

    else:
        response.status_code = 400
        response.content = "Wrong Method"


def generate_parameter(request, key):
    # return the params of the request

    if request.method == "GET":
        return request.GET.get(key)

    elif request.method == "POST":
        return request.POST.get(key)

    return None


def get_all_messages(limit=-1, offset=0) -> []:
    if limit == -1:
        return models.Message.objects.all()[offset:]
    else:
        return models.Message.objects.all()[offset:offset + limit]


def get_messages_unread_by_user_name(user_name: str, limit: int = - 1, offset: int = 0) -> []:
    # return the message unread by the user
    user = get_user_by_user_name(user_name)
    user_message = models.User_Message.objects.values('message_id').filter(user_id=user.id)
    user_message_list = [i['message_id'] for i in user_message]
    if limit == -1:
        return models.Message.objects.exclude(id__in=user_message_list)[offset:]
    else:
        return models.Message.objects.exclude(id__in=user_message_list)[offset:offset + limit]


def get_user_by_user_name(user_name: str) -> models.User:
    if not models.User.objects.filter(name=user_name).exists():
        raise Exception("User not exists", user_name)

    return models.User.objects.get(name=user_name)



