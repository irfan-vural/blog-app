# Generated by Django 4.0.4 on 2022-04-26 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publis_date',
            new_name='publis',
        ),
    ]