# login/models.py
from django.db import models
class User(models.Model):
    '''用户表'''
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=128, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=256, verbose_name="密码")
    email = models.EmailField(unique=True, verbose_name="电子邮件")
    c_time = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")
    phone = models.CharField(max_length=11, verbose_name="手机号")
    layout = models.IntegerField(verbose_name='布局设置', default=4)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Video(models.Model):
    '视频源'
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user_id = models.ForeignKey(to='User', to_field='id', on_delete=models.CASCADE, verbose_name='用户名')
    video_url = models.CharField(max_length=256, verbose_name='视频地址')

class Device(models.Model):
    '设备'
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='设备号')
    serial_number = models.CharField(max_length=128, unique=True, verbose_name='设备序列号')
    location_x = models.FloatField(verbose_name='经度')
    location_y = models.FloatField(verbose_name='纬度')
    hint = models.CharField(max_length=128, verbose_name='标识')
    video_url = models.CharField(max_length=256, verbose_name='视频地址', default='')


class Message(models.Model):
    '消息流'
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    content = models.CharField(max_length=256,verbose_name='告警信息')
    img_url = models.CharField(max_length=256, verbose_name='图片链接')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')
    serial_number = models.ForeignKey(to='Device', to_field='serial_number', verbose_name='设备号', on_delete=models.CASCADE)


class User_Message(models.Model):
    '用户审核信息'
    user_id = models.ForeignKey(to='User', to_field='id', on_delete=models.CASCADE, verbose_name='用户名')
    message_id = models.ForeignKey(to='Message', to_field='id', on_delete=models.CASCADE, verbose_name='信息id')
    true_or_false = models.BooleanField(verbose_name='预警正误')


