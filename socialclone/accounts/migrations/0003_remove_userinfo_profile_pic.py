# Generated by Django 4.0.5 on 2022-06-21 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userinfo_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='profile_pic',
        ),
    ]