# Generated by Django 5.1.3 on 2024-12-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
