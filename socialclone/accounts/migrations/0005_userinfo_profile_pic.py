# Generated by Django 4.0.5 on 2022-06-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_userinfo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
