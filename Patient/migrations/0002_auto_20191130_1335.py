# Generated by Django 2.2.6 on 2019-11-30 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='prescriptionIssueDate',
            field=models.CharField(max_length=33),
        ),
    ]