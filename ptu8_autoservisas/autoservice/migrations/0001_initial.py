# Generated by Django 4.1.7 on 2023-02-22 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_registration_plate', models.CharField(max_length=10, verbose_name='vehicle registration plate')),
                ('vehicle_identification_number', models.CharField(max_length=17, verbose_name='vehicle identification number')),
                ('client', models.CharField(max_length=30, verbose_name='client')),
            ],
            options={
                'ordering': ['client', 'vehicle_registration_plate'],
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(db_index=True, max_length=100, verbose_name='make')),
                ('model', models.CharField(db_index=True, max_length=100, verbose_name='model')),
            ],
            options={
                'ordering': ['make', 'model'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='order date')),
                ('status', models.CharField(choices=[('o', 'ordered'), ('p', 'in process'), ('d', 'done'), ('c', 'cancelled')], default='o', max_length=1, verbose_name='status')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='autoservice.car', verbose_name='car')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='price')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_lines', to='autoservice.order', verbose_name='orders')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_lines', to='autoservice.service', verbose_name='service')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='autoservice.carmodel', verbose_name='model'),
        ),
    ]
