# Generated by Django 3.0.5 on 2020-05-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200510_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='added_by',
            field=models.CharField(default='----', max_length=20),
        ),
    ]
