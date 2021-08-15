# Generated by Django 3.2.6 on 2021-08-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('middle_name', models.CharField(max_length=50)),
                ('first_login', models.DateTimeField(null=True)),
                ('phone', models.CharField(max_length=14)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user/avatar/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
