# Generated by Django 4.2.2 on 2023-06-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plate', '0002_alter_platemodel_license_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='platemodel',
            name='status',
            field=models.CharField(blank=True, choices=[('ADMITED', 'admited'), ('BANNED', 'banned')], default='ADMITED', max_length=255),
        ),
    ]
