# Generated by Django 2.1.4 on 2019-03-05 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personName', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='todo',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
    ]