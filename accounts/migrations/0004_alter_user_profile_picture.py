# Generated by Django 5.1.3 on 2024-12-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='/statitc/default-profile.jpg', upload_to='profile_pictures/'),
        ),
    ]
