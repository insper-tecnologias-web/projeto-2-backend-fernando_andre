# Generated by Django 5.0.3 on 2024-03-12 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_remove_note_tag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
