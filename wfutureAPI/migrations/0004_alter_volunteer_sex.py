# Generated by Django 5.0.6 on 2024-07-05 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wfutureAPI', '0003_storeitem_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='sex',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('prefer_not_to_say', 'Prefer not to say')], max_length=50, null=True),
        ),
    ]