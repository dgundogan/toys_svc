# Generated by Django 3.0.4 on 2020-03-28 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200327_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='DroneCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=2)),
                ('races_count', models.IntegerField()),
                ('inserted_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('manufacturing_date', models.DateTimeField()),
                ('has_it_competed', models.BooleanField(default=False)),
                ('inserted_timestamp', models.DateTimeField(auto_now_add=True)),
                ('drone_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drones', to='core.DroneCategory')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_in_feet', models.IntegerField()),
                ('distance_achievement_date', models.DateTimeField()),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Drone')),
                ('pilot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competitions', to='core.Pilot')),
            ],
            options={
                'ordering': ('-distance_in_feet',),
            },
        ),
    ]
