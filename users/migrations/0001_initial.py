# Generated by Django 4.0.2 on 2022-03-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('Time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
