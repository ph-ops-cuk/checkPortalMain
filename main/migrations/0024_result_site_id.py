# Generated by Django 3.2 on 2021-04-27 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20210427_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='site_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.site'),
        ),
    ]