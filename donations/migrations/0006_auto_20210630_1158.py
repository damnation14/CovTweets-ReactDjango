# Generated by Django 3.2.4 on 2021-06-30 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0005_auto_20210630_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='Account_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='donations',
            name='Phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
