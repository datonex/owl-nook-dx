# Generated by Django 3.2 on 2022-05-02 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='bookmark',
            old_name='list_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
    ]
