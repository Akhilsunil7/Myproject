# Generated by Django 4.1.7 on 2023-05-06 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Pimg')),
            ],
        ),
    ]