# Generated by Django 3.0.5 on 2020-05-31 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200531_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]