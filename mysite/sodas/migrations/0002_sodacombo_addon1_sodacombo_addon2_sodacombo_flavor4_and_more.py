# Generated by Django 5.0.3 on 2024-04-26 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sodas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sodacombo',
            name='addon1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sodacombo',
            name='addon2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sodacombo',
            name='flavor4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sodacombo',
            name='splash',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
