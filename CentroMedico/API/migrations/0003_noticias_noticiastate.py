# Generated by Django 4.2.1 on 2023-06-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_remove_noticias_typenoticeid_remove_users_typeuserid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='NoticiaState',
            field=models.BooleanField(default=False),
        ),
    ]