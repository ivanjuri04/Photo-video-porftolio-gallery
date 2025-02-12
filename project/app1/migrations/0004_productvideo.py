# Generated by Django 5.0.6 on 2024-07-31 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_firstproductpicture_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/clips')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app1.firstproductpicture')),
            ],
            options={
                'verbose_name': 'productvideo',
                'verbose_name_plural': 'product video',
            },
        ),
    ]
