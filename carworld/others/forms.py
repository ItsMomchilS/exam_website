import os
from os.path import join

from django import forms
from django.conf import settings

from carworld.core.forms import BootstrapFormMixin
from carworld.others.models import Source


class SourceForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Source
        exclude = ('name',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'some-class',
                }
            )
        }


class EditSourceForm(SourceForm):
    def save(self, commit=True):
        db_source = Source.objects.get(pk=self.instance.id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_source.image))
            os.remove(image_path)
        return super().save(commit)

    class Meta:
        model = Source
        fields = '__all__'


