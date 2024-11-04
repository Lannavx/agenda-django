from django import forms
from . import models
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
  first_name = forms.CharField(
    widget=forms.TextInput(
      attrs={'placeholder': 'Escreva aqui'}
    ),
    help_text= 'Texto de ajuda para o usuário',
  )

  class Meta:
    model = models.Contact
    fields = (
      'first_name', 'last_name', 'phone', 
      'email', 'description', 'category',
      )

  def clean(self):
    cleaned_data = self.cleaned_data
    first_name = cleaned_data.get('first_name')
    last_name = cleaned_data.get('last_name')

    if first_name == last_name:
      msg = ValidationError(
          'Primeiro nome não pode ser igual ao segundo', code='invalid')
      self.add_error('first_name', msg)
      self.add_error('last_name', msg)

    return super().clean()

  