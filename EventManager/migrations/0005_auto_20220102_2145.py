# Generated by Django 3.2.3 on 2022-01-02 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EventManager', '0004_participant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='event',
        ),
        migrations.AddField(
            model_name='participant',
            name='participant_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventManager.event'),
        ),
    ]
