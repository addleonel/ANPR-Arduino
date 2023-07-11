# Generated by Django 4.2.2 on 2023-07-11 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plate', '0005_alter_platemodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlateCapturedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(blank=True, max_length=255, null=True)),
                ('image_license', models.ImageField(blank=True, max_length=300, null=True, upload_to='img/output_photos/')),
                ('image_car', models.ImageField(blank=True, max_length=300, null=True, upload_to='img/car_captured/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]