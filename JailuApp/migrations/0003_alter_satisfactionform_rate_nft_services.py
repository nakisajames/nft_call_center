# Generated by Django 4.0.2 on 2023-05-17 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JailuApp', '0002_satisfactionform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satisfactionform',
            name='rate_nft_services',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
