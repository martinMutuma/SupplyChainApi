# Generated by Django 4.2.2 on 2023-06-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_supplychainitem_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplychainitem',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
