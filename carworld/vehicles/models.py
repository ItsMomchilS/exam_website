from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

UserModel = get_user_model()


class Vehicle(models.Model):
    AD_TYPE_SELL = 'Selling:'
    AD_TYPE_BUY = 'Looking for:'

    AD_CHOICES = (
        (AD_TYPE_SELL, 'Selling car'),
        (AD_TYPE_BUY, 'Looking for car'),
    )

    TYPE_CHOICE_CAR = 'car'
    TYPE_CHOICE_SUV = 'suv'
    TYPE_CHOICE_MOTORCYCLE = 'motorcycle'
    TYPE_CHOICE_OTHER = 'others'

    TYPE_CHOICES = (
        (TYPE_CHOICE_CAR, 'Car'),
        (TYPE_CHOICE_SUV, 'SUV'),
        (TYPE_CHOICE_MOTORCYCLE, 'Motorcycle'),
        (TYPE_CHOICE_OTHER, 'Other')
    )

    type = models.CharField(
        max_length=15,
        choices=TYPE_CHOICES,
    )

    ad_type = models.CharField(
        max_length=15,
        choices=AD_CHOICES,
    )

    vehicle_model = models.CharField(
        max_length=15,
    )
    create_year = models.PositiveIntegerField(
        default=2000,
        validators=[
            MaxValueValidator(2021),
            MinValueValidator(1940),
        ],
     )
    price = models.PositiveIntegerField()

    description = models.TextField()
    image = models.ImageField(
        upload_to='vehicles',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.ad_type}, {self.type}, {self.vehicle_model}, {self.create_year}'


class Like(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
