from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register(request):
  '''Registra um novo usuário. Se o formulário for válido, salva o usuário e 
  o redireciona para a página de login'''
  form = RegisterForm()

  if request.method == 'POST':
    form = RegisterForm(request.POST)

    if form.is_valid():
      form.save()
      messages.success(request, 'Usuário registrado com sucesso!')
      return redirect('contact:login')

  return render(
    request,
    'contact/register.html',
    {
      'form': form
    }
  )

@login_required(login_url='contact:login')
def user_update(request):
  '''Atualização dos dados do usuário autenticado. Exibe um formulário 
  pré-preenchido com os dados do usuário. Processa as alterações submetidas 
  e salva as atualizações'''
  form = RegisterUpdateForm(instance=request.user)

  if request.method != 'POST': 
    return render(
    request,
    'contact/user_update.html',
    {
      'form': form
    }
    )
   
  form = RegisterUpdateForm(data=request.POST, instance=request.user)

  if not form.is_valid():
    return render(
    request,
    'contact/user_update.html',
    {
      'form': form
    }
  )

  form.save()
  return redirect('contact:user_update')


def login_view(request):
  '''Autenticação de usuários.Processa as credenciais de login e se válidas,
  loga o usuário'''
  form = AuthenticationForm(request)

  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
      user = form.get_user()
      auth.login(request, user)
      messages.success(request, 'Usuário logado com sucesso!')
      return redirect('contact:index')
    messages.error(request, 'Login inválido')

  return render(
    request,
    'contact/login.html',
    {
      'form': form
    }
  )

@login_required(login_url='contact:login')
def logout_view(request):
  '''Desconecta o usuário atual e o redireciona para a página de login'''
  auth.logout(request)
  return redirect('contact:login')