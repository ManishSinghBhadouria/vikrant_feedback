# Generated by Django 3.0.2 on 2020-03-20 12:24

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('mobile', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('pwd', models.CharField(max_length=100)),
            ],
        ),
    ]
