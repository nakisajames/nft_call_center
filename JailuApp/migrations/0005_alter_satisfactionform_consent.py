# Generated by Django 4.0.2 on 2023-05-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JailuApp', '0004_satisfactionform_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satisfactionform',
            name='consent',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]