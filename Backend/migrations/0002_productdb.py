# Generated by Django 5.0.5 on 2024-05-13 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CY_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('ProductName', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('ProductImage', models.ImageField(blank=True, null=True, upload_to='Product Images')),
            ],
        ),
    ]
