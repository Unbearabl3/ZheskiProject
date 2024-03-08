# Generated by Django 4.2.7 on 2024-03-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=24, verbose_name='Username')),
                ('Password', models.CharField(max_length=32, verbose_name='Password')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
    ]