# Generated by Django 4.0.1 on 2022-12-25 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_alter_tguser_verification_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tguser',
            options={'verbose_name': 'TG User', 'verbose_name_plural': 'TG Users'},
        ),
    ]
