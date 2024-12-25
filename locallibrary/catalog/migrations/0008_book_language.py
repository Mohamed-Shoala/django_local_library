# Generated by Django 5.1.2 on 2024-12-25 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_rename_autor_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Select the language of the book', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.language'),
        ),
    ]