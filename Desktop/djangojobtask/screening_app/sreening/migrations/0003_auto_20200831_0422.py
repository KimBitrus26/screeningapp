# Generated by Django 3.1 on 2020-08-31 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sreening', '0002_auto_20200831_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(blank=True, default=None, help_text='Input a question', max_length=800),
        ),
    ]
