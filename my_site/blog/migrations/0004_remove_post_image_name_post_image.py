# Generated by Django 4.2.7 on 2024-02-14 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author_post_tag_alter_tag_caption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_name',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
