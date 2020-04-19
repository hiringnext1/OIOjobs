# Generated by Django 2.2 on 2020-04-19 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobopening', '0002_auto_20200419_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobopening',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='employment_type',
            field=models.CharField(blank=True, max_length=100, verbose_name='Employment Type'),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='job_created',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='job_location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Job Location'),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='max_salary_budget',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Mention Salary in Annual Packages only', max_digits=10, null=True, verbose_name='Max. Salary Criteria'),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='min_salary_budget',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Mention Salary in Annual Packages only', max_digits=10, null=True, verbose_name='Min. Salary Criteria'),
        ),
        migrations.AlterField(
            model_name='jobopening',
            name='role_category',
            field=models.CharField(blank=True, max_length=50, verbose_name='Role Category'),
        ),
    ]
