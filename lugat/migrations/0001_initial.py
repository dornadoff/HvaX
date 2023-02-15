# Generated by Django 4.1.6 on 2023-02-03 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Togri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soz', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NoTogri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notogri', models.CharField(max_length=100)),
                ('t_soz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lugat.togri')),
            ],
        ),
    ]