# Generated by Django 3.2.3 on 2021-08-08 19:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('car', 'Car'), ('suv', 'SUV'), ('motorcycle', 'Motorcycle'), ('others', 'Other')], max_length=15)),
                ('ad_type', models.CharField(choices=[('Selling:', 'Selling car'), ('Looking for:', 'Looking for car')], max_length=15)),
                ('vehicle_model', models.CharField(max_length=15)),
                ('create_year', models.PositiveIntegerField(default=2000, validators=[django.core.validators.MaxValueValidator(2021), django.core.validators.MinValueValidator(1940)])),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='vehicles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
    ]
