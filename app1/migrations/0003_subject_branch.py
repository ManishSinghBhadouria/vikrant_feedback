# Generated by Django 3.0.2 on 2020-04-01 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='branch',
            field=models.CharField(default=12365, max_length=100),
            preserve_default=False,
        ),
    ]
