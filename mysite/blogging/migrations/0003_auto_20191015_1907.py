# Generated by Django 2.1.1 on 2019-10-16 02:07

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('blogging', '0002_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
    ]
