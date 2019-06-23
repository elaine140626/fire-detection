from django.shortcuts import render
from . import models
from .forms import UserForm
from django.core import serializers
import json
import datetime

# Create your views here.

from django.shortcuts import render,redirect


def warning(request):

    ret_vars = {}

    if request.session.get('is_login', None):
        ret_vars['username']=request.session['user_name']

        user = models.User.objects.get(name = request.session['user_name'])
        user_message = models.User_Message.objects.values('message_id').filter(user_id=user.id)
        user_message_dict = {i.message_id:'true' for i in user_message }
        print(user_message_dict)
        message_list = models.Message.objects.all()

        user_message_list = [{
            'id':i.id,
            'content':i.content,
            'img_url':i.img_url,
            'device_number':i.serial_number.id,
            'device_hint':i.serial_number.hint,
            'deal':i.id in user_message_dict,
            'c_time':i.c_time.strftime('%Y-%m-%d %H:%M:%S')
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
        ret_vars['username']=request.session['user_name']

        user = models.User.objects.get(name=request.session['user_name'])
        user_message = models.User_Message.objects.values('message_id').filter(user_id=user.id)
        user_message_list = [i.message_id for i in user_message ]
        message_list = models.Message.objects.exclude(id__in=user_message_list)[:10]

        ret_vars['message_list'] = serializers.serialize('json', message_list)

        return render(request, 'overview.html', ret_vars)

    return redirect('/login')

def monitor(request):

    ret_vars = {}

    if request.session.get('is_login', None):
        ret_vars['username']=request.session['user_name']
        user = models.User.objects.get(name=request.session['user_name'])
        video_list = models.Video.objects.filter(user_id= user.id)
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
