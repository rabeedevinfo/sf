# Generated by Django 3.2.25 on 2025-03-14 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createassoc', '0006_alter_code_koraa_date_fin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code_koraa',
            name='date_fin',
            field=models.DateField(blank=True, null=True),
        ),
    ]
