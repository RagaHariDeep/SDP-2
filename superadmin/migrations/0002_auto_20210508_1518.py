# Generated by Django 3.2.1 on 2021-05-08 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='superadminlogin',
            fields=[
                ('email', models.EmailField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'admindata',
            },
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='no_of_days_advance',
        ),
    ]
