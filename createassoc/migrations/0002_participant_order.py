# Generated by Django 3.2.25 on 2025-02-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createassoc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
