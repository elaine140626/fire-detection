# Generated by Django 2.2.2 on 2019-06-17 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='设备号')),
                ('location_x', models.FloatField(verbose_name='经度')),
                ('location_y', models.FloatField(verbose_name='纬度')),
                ('hint', models.CharField(max_length=128, verbose_name='标识')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=256, verbose_name='告警信息')),
                ('img_url', models.CharField(max_length=256, verbose_name='图片链接')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('serial_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Device', verbose_name='设备号')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='电子邮件')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('layout', models.IntegerField(default=4, verbose_name='布局设置')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['c_time'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.CharField(max_length=256, verbose_name='视频地址')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User', verbose_name='用户名')),
            ],
        ),
        migrations.CreateModel(
            name='User_Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('true_or_false', models.BooleanField(verbose_name='预警正误')),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Message', verbose_name='信息id')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User', verbose_name='用户名')),
            ],
        ),
    ]
