# Generated by Django 5.0.6 on 2024-07-17 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstproductpicture',
            name='images',
            field=models.ImageField(upload_to='photos/pictures'),
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='photos/pictures')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app1.firstproductpicture')),
            ],
            options={
                'verbose_name': 'productgallery',
                'verbose_name_plural': 'product gallery',
            },
        ),
    ]
