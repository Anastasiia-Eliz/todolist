# Generated by Django 4.0.1 on 2022-12-20 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_user_id', models.IntegerField(verbose_name='ID пользователя в телеграм')),
                ('tg_chat_id', models.IntegerField(verbose_name='ID чата в телеграм')),
                ('verification_code', models.IntegerField(verbose_name='Код для верификации')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь приложения')),
            ],
            options={
                'verbose_name': 'Пользователь телеграм',
                'verbose_name_plural': 'Пользователи телеграм',
            },
        ),
    ]
