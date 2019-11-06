# Generated by Django 2.2.6 on 2019-11-04 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storeName', models.CharField(max_length=25)),
                ('licence', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=50)),
                ('storeAddress', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]