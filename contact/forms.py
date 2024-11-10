from django import forms
from . import models
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class ContactForm(forms.ModelForm):
  '''Formulário para criação e atualização de contatos

    Este formulário é baseado no modelo Contact e inclui campos para:
    - Primeiro nome 
    - Sobrenome
    - Telefone
    - E-mail
    - Descrição
    - Categoria
    - Foto (opcional)

    Validações personalizadas:
    - Verifica se o primeiro nome não é igual ao sobrenome.'''
  picture = forms.ImageField(
    widget=forms.FileInput(
      attrs={
        'accept': 'image/*'
      }
    ), 
    required=False
  )

  class Meta:
    model = models.Contact
    fields = (
      'first_name', 'last_name', 'phone', 
      'email', 'description', 'category',
      'picture',
      )

  def clean(self):
    '''Método de limpeza dos dados do formulário. Verifica se o primeiro 
    nome e o sobrenome não são iguais. Se forem iguais, adiciona um erro de 
    validação aos campos correspondentes'''
    cleaned_data = self.cleaned_data
    first_name = cleaned_data.get('first_name')
    last_name = cleaned_data.get('last_name')

    if first_name == last_name:
      msg = ValidationError(
          'Primeiro nome não pode ser igual ao segundo', code='invalid')
      self.add_error('first_name', msg)
      self.add_error('last_name', msg)

    return super().clean()

class RegisterForm(UserCreationForm):
  '''Formulário para registro de novos usuários

    Extende o formulário padrão UserCreationForm do Django, adicionando 
    campos obrigatórios para:
    - Primeiro nome
    - Sobrenome
    - E-mail

    Validações personalizadas:
    - Verifica se o e-mail já está em uso por outro usuário.'''
  first_name = forms.CharField(
    required=True
  )

  last_name = forms.CharField(
    required=True
  )

  email = forms.EmailField(
    required=True
  )

  class Meta:
    model = User
    fields = (
      'first_name', 'last_name', 'email', 
      'username', 'password1', 'password2',
    )

  def clean_email(self):
    '''Valida o campo de e-mail, verificando se o e-mail fornecido já está 
    registrado no sistema. Se estiver, adiciona um erro de validação 
    ao campo de e-mail'''
    email = self.cleaned_data.get('email')

    if User.objects.filter(email=email).exists():
      self.add_error(
        'email',
        ValidationError(
          'Uma conta com este endereço de e-mail já existe',
          code='invalid'
        )
      )

    return email
  
class RegisterUpdateForm(forms.ModelForm):
  '''Formulário para atualização dos dados do usuário registrado

    Inclui campos para:
    - Primeiro nome
    - Sobrenome
    - E-mail
    - Nome de usuário
    - Senha (opcional)
    - Confirmação de senha (opcional)

    Validações personalizadas:
    - Verifica se as senhas correspondem ao atualizar.
    - Verifica se o e-mail é único ao atualizar.
    - Valida a força da nova senha.'''
  first_name = forms.CharField(
    min_length=2,
    max_length=30,
    required=True,
    help_text='Required.',
    error_messages={
        'min_length': 'Please, add more than 2 letters.'
    }
)
  last_name = forms.CharField(
    min_length=2,
    max_length=30,
    required=True,
    help_text='Required.'
)

  password1 = forms.CharField(
    label="Password",
    strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    help_text=password_validation.password_validators_help_text_html(),
    required=False,
)

  password2 = forms.CharField(
    label="Password 2",
    strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    help_text='Use the same password as before.',
    required=False,
)

  class Meta:
    model = User
    fields = (
        'first_name', 'last_name', 'email',
        'username',
    )

  def save(self, commit=True):
    ''' Salva o usuário com os dados atualizados. Se uma nova senha for 
    fornecida, atualiza a senha do usuário'''
    cleaned_data = self.cleaned_data
    user = super().save(commit=False)
    password = cleaned_data.get('password1')

    if password:
      user.set_password(password)

    if commit:
      user.save()

    return user

  def clean(self):
    ''' Valida os dados do formulário, verificando se as senhas 
    correspondem quando fornecidas'''
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')

    if password1 or password2:
      if password1 != password2:
        self.add_error(
            'password2',
            ValidationError('As senhas não correspondem')
        )

    return super().clean()

  def clean_email(self):
    ''' Valida o campo de e-mail e verifica se o e-mail fornecido já está
    em uso por outro usuário ao atualizar o perfil'''
    email = self.cleaned_data.get('email')
    current_email = self.instance.email

    if current_email != email:
      if User.objects.filter(email=email).exists():
        self.add_error(
            'email',
            ValidationError('Já existe este e-mail', code='invalid')
        )

      return email

  def clean_password1(self):
    '''Valida a força da nova senha. Se uma nova senha for fornecida, 
    valida usando os validadores padrão do Django'''
    password1 = self.cleaned_data.get('password1')

    if password1:
      try:
        password_validation.validate_password(password1)
      except ValidationError as errors:
        self.add_error(
            'password1',
            ValidationError(errors)
        )

    return password1