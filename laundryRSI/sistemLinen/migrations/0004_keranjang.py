# Generated by Django 3.1.2 on 2021-11-23 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemLinen', '0003_transaksi_status_konfirmasi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keranjang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaksi', models.IntegerField()),
                ('linen', models.CharField(max_length=20)),
                ('jumlah', models.IntegerField()),
                ('waktu', models.DateTimeField()),
            ],
        ),
    ]