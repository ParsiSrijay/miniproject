# Generated by Django 3.0.1 on 2020-02-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200218_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=10)),
                ('CropName', models.CharField(max_length=10)),
                ('CropType', models.CharField(max_length=10)),
                ('Quantity', models.IntegerField()),
                ('Quality', models.ImageField(upload_to='images/')),
            ],
        ),
    ]