# Generated by Django 3.1.2 on 2021-11-22 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemLinen', '0002_remove_detail_transaksi_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaksi',
            name='status_konfirmasi',
            field=models.BooleanField(default=False),
        ),
    ]
