# Generated by Django 3.0.7 on 2020-06-26 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200626_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='staus',
            field=models.BooleanField(default=False),
        ),
    ]
