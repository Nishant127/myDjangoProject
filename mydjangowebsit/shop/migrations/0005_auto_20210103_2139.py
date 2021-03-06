# Generated by Django 3.1.1 on 2021-01-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('zip_code', models.CharField(max_length=150)),
                ('phone', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
