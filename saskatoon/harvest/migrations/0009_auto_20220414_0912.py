# Generated by Django 3.2.9 on 2022-04-14 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('harvest', '0008_auto_20220406_1647'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='harvest',
            options={'ordering': ['-start_date'], 'verbose_name': 'harvest', 'verbose_name_plural': 'harvests'},
        ),
        migrations.AlterField(
            model_name='harvest',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='harvests', to='harvest.property', verbose_name='Property'),
        ),
        migrations.AlterField(
            model_name='requestforparticipation',
            name='harvest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='harvest.harvest', verbose_name='Harvest'),
        ),
    ]