# Generated by Django 2.1.2 on 2019-01-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_auto_20181231_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardcomment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
