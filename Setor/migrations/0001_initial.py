# Generated by Django 5.1.5 on 2025-01-26 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
