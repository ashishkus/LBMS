# Generated by Django 2.2a1 on 2019-12-19 13:30

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1000)])),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1000)])),
                ('branch', models.CharField(default='', max_length=13)),
                ('rollno', models.CharField(max_length=8)),
                ('issuingdate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('issuingstatus', models.CharField(choices=[('issued', 'ISSUED'), ('not_issued', 'NOT_ISSUED')], default='', max_length=10)),
                ('returningstatus', models.CharField(choices=[('returned', 'RETURNED'), ('not_returned', 'NOT_RETURNED')], default='', max_length=10)),
                ('DUE_DATE', models.DateField(verbose_name=models.DateField(default=datetime.date.today, verbose_name='Date'))),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=26)),
            ],
        ),
        migrations.CreateModel(
            name='COMPSBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('bookname', models.CharField(max_length=130)),
                ('year', models.CharField(default='', max_length=2)),
                ('bookid', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(5000), django.core.validators.MinValueValidator(3001)])),
                ('publisher', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ELECTRONICSBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('bookname', models.CharField(max_length=130)),
                ('year', models.CharField(default='', max_length=2)),
                ('bookid', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(9000), django.core.validators.MinValueValidator(7001)])),
                ('publisher', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EXTCBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('bookname', models.CharField(max_length=130)),
                ('year', models.CharField(default='', max_length=2)),
                ('bookid', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(7000), django.core.validators.MinValueValidator(5001)])),
                ('publisher', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('bookname', models.CharField(max_length=130)),
                ('year', models.CharField(default='', max_length=2)),
                ('bookid', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(9501)])),
                ('publisher', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='INSTRUBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('bookname', models.CharField(max_length=130)),
                ('year', models.CharField(default='', max_length=2)),
                ('bookid', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(9500), django.core.validators.MinValueValidator(9001)])),
                ('publisher', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ITBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('bookname', models.CharField(max_length=130)),
                ('year', models.CharField(default='', max_length=2)),
                ('bookid', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(3000), django.core.validators.MinValueValidator(1000)])),
                ('publisher', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='searching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=12)),
            ],
        ),
    ]