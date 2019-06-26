# Generated by Django 2.2.2 on 2019-06-26 11:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='serial_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=128, unique=True, verbose_name='设备序列号'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='serial_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Device', to_field='serial_number', verbose_name='设备号'),
        ),
    ]