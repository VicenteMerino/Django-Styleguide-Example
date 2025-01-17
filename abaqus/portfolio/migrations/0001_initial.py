# Generated by Django 4.1.7 on 2023-04-19 19:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioAsset',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('weight', models.DecimalField(decimal_places=4, max_digits=10)),
                ('date', models.DateField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_assets', to='portfolio.asset')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_assets', to='portfolio.portfolio')),
            ],
            options={
                'unique_together': {('portfolio', 'asset', 'date')},
            },
        ),
        migrations.AddField(
            model_name='portfolio',
            name='assets',
            field=models.ManyToManyField(related_name='portfolios', through='portfolio.PortfolioAsset', to='portfolio.asset'),
        ),
        migrations.CreateModel(
            name='AssetPrice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='portfolio.asset')),
            ],
            options={
                'unique_together': {('asset', 'date')},
            },
        ),
    ]
