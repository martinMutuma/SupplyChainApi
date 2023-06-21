# Generated by Django 4.2.2 on 2023-06-21 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0004_alter_supplychainitem_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventStatus',
            fields=[
                ('id', models.AutoField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_%(app_label)s_%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_%(app_label)s_%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SupplyChainEvent',
            fields=[
                ('id', models.AutoField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('action', models.CharField(blank=True, max_length=255)),
                ('additional_parties_involved', models.TextField(blank=True)),
                ('documentation', models.URLField(blank=True)),
                ('signature', models.CharField(blank=True, max_length=255)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_%(app_label)s_%(class)s', to=settings.AUTH_USER_MODEL)),
                ('custodian', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='custodian', to=settings.AUTH_USER_MODEL)),
                ('event_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_status', to='supplyChainEvents.eventstatus')),
                ('event_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_type', to='supplyChainEvents.eventtype')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.supplychainitem')),
                ('next_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)snext_event', to='supplyChainEvents.supplychainevent')),
                ('parent_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)sparent_event', to='supplyChainEvents.supplychainevent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
