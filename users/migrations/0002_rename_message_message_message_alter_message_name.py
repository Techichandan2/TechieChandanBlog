# Generated by Django 4.0.2 on 2022-03-16 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='Message',
        ),
        migrations.AlterField(
            model_name='message',
            name='Name',
            field=models.CharField(max_length=50),
        ),
    ]
