# Generated by Django 4.1.3 on 2022-12-12 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LichTietKhi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tietkhi', models.CharField(max_length=255)),
                ('daytiekhi', models.CharField(max_length=255)),
                ('year', models.IntegerField(default=0)),
                ('month', models.IntegerField(default=0)),
            ],
        ),
    ]
