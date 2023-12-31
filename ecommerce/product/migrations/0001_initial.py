# Generated by Django 4.2.4 on 2023-08-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoapItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('cat', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='Soap_image')),
                ('price', models.FloatField()),
                ('Quantity', models.IntegerField()),
                ('Available', models.BooleanField(default=True)),
            ],
        ),
    ]
