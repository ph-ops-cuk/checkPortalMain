# Generated by Django 3.2 on 2021-04-28 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_result_site_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category'),
        ),
    ]
