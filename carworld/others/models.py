from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Source(models.Model):
    image = models.ImageField(
        upload_to='others',
    )

    name = models.CharField(
        max_length=50,
    )
    url = models.URLField(
        max_length=200,
    )

    description = models.TextField()

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}, {self.url}, {self.image}'