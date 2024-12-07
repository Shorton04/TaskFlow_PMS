# Generated by Django 5.1.3 on 2024-12-05 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_full_name_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('project_member', 'Project Member'), ('project_manager', 'Project Manager')], default='project_manager', max_length=50),
        ),
    ]
