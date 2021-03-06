# Generated by Django 3.0.3 on 2020-02-12 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ShipClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('typ', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=20)),
                ('numGuns', models.IntegerField()),
                ('bore', models.FloatField()),
                ('displacement', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('launched', models.IntegerField()),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sql.ShipClass')),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outcome', models.CharField(max_length=10)),
                ('battle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sql.Battle')),
                ('ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sql.Ship')),
            ],
        ),
    ]
