# Generated by Django 3.2.3 on 2022-01-02 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventManager', '0005_auto_20220102_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='name',
            new_name='event_name',
        ),
    ]