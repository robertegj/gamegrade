# Generated by Django 3.0.7 on 2020-06-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='grade',
            field=models.IntegerField(default=0),
        ),
    ]
