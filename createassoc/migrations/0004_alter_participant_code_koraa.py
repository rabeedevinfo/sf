# Generated by Django 3.2.25 on 2025-03-04 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('createassoc', '0003_alter_participant_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='code_koraa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participants', to='createassoc.code_koraa'),
        ),
    ]
