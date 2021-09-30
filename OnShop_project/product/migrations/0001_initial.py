# Generated by Django 3.1.7 on 2021-09-30 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='images/default_product.png', upload_to='images/products')),
            ],
        ),
    ]
