# Generated by Django 3.2 on 2021-04-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210427_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='check_frequency',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], default='Daily', max_length=200, null=True),
        ),
    ]