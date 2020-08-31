# Generated by Django 3.1 on 2020-08-31 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sreening', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_body',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='questions',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='sreening.question'),
        ),
    ]
