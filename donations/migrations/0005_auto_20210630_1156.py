# Generated by Django 3.2.4 on 2021-06-30 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0004_rename_content_donations_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donations',
            name='donationoptions',
        ),
        migrations.AddField(
            model_name='donations',
            name='Account_no',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='donations',
            name='Phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
