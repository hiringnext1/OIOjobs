# Generated by Django 2.2 on 2020-04-18 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='relevant_industry',
        ),
    ]
