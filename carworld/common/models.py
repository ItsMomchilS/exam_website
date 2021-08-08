from django.contrib.auth import get_user_model
from django.db import models

from carworld.vehicles.models import Vehicle

UserModel = get_user_model()


class Comment(models.Model):
    text = models.TextField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
