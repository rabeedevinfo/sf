# Generated by Django 3.2.25 on 2025-03-14 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createassoc', '0004_alter_participant_code_koraa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code_koraa',
            name='date_fin',
            field=models.DateField(null=True),
        ),
    ]
