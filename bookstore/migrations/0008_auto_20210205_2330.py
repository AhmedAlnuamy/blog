# Generated by Django 3.1.5 on 2021-02-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0007_auto_20210202_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='advater',
            field=models.ImageField(blank=True, default='person1.jpg', null=True, upload_to=''),
        ),
    ]
