# Generated by Django 3.0.7 on 2020-08-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0014_record_abstract_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='abstract_file',
            field=models.FileField(blank=True, null=True, upload_to='abstract/'),
        ),
    ]
