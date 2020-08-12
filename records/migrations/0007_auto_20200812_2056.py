# Generated by Django 3.0.7 on 2020-08-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_auto_20200808_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorrole',
            name='name',
            field=models.CharField(choices=[('presenter', 'Presenter'), ('adviser', 'Adviser'), ('researcher', 'Researcher')], max_length=100),
        ),
    ]
