# Generated by Django 4.0.5 on 2022-07-24 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=200),
            preserve_default=False,
        ),
    ]