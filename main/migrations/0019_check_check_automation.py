# Generated by Django 3.2 on 2021-04-27 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_check_check_frequency'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='check_automation',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], default='Manual', max_length=200, null=True),
        ),
    ]
