# Generated by Django 3.1 on 2020-08-31 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sreening', '0004_auto_20200831_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_body',
            field=models.CharField(blank=True, help_text='Input a question', max_length=800),
        ),
    ]
