# Generated by Django 3.2.4 on 2021-06-12 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]