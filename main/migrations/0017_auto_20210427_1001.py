# Generated by Django 3.2 on 2021-04-27 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_result_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='category_id',
        ),
        migrations.AddField(
            model_name='result',
            name='incident_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.incident'),
        ),
    ]
