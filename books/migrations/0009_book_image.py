# Generated by Django 4.0.1 on 2022-02-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
