import os
from os.path import join

from django import forms
from django.conf import settings

from carworld.core.forms import BootstrapFormMixin
from carworld.vehicles.models import Vehicle


class VehicleForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ('user',)
        widgets = {
            'vehicle_model': forms.TextInput(
                attrs={
                    'class': 'some-class',
                }
            )
        }


class EditVehicleForm(VehicleForm):
    def save(self, commit=True):
        db_vehicle = Vehicle.objects.get(pk=self.instance.id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_vehicle.image))
            os.remove(image_path)
        return super().save(commit)

    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }
