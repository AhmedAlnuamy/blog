# Generated by Django 3.1.5 on 2021-01-27 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=190, null=True)),
                ('Email', models.CharField(max_length=190, null=True)),
                ('phone', models.CharField(max_length=190, null=True)),
                ('Age', models.CharField(max_length=190, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]