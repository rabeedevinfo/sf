# Generated by Django 3.2.25 on 2025-03-18 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createassoc', '0007_alter_code_koraa_date_fin'),
    ]

    operations = [
        migrations.AddField(
            model_name='code_koraa',
            name='montant_part',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
