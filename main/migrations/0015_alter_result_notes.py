# Generated by Django 3.2 on 2021-04-26 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210426_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='notes',
            field=models.CharField(default='null', max_length=500, null=True),
        ),
    ]
