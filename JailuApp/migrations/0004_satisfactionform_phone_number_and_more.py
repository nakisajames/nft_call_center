# Generated by Django 4.0.2 on 2023-05-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JailuApp', '0003_alter_satisfactionform_rate_nft_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='satisfactionform',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='satisfactionform',
            name='status',
            field=models.TextField(blank=True, max_length=15, null=True),
        ),
    ]
