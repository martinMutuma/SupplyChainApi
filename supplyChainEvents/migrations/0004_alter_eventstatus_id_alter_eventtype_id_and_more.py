# Generated by Django 4.2.2 on 2023-06-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplyChainEvents', '0003_eventstatus_color_alter_eventtype_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventstatus',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='supplychainevent',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
