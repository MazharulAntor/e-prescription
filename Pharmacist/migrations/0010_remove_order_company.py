# Generated by Django 2.2.6 on 2019-11-23 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pharmacist', '0009_medicinestock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='company',
        ),
    ]