# Generated by Django 4.2.2 on 2023-06-29 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplyChainEvents', '0006_alter_supplychainevent_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventstatus',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
