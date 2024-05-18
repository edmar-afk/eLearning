# Generated by Django 5.0.4 on 2024-05-17 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_comments_comment_date_alter_forum_upload_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 17, 12, 27, 20, 247368, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 17, 12, 27, 20, 247368, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 17, 12, 27, 20, 247368, tzinfo=datetime.timezone.utc)),
        ),
    ]