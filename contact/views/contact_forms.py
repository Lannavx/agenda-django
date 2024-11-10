from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact
from django.contrib.auth.decorators import login_required

@login_required(login_url='contact:login')
def create(request):
  '''Permite que usuários autenticados criem um novo contato através de 
  um formulário. Se a requisição for via POST e o formulário for válido, 
  o contato é salvo associado ao usuário atual, e o usuário é redirecionado 
  para a página de atualização desse contato'''
  form_action = reverse('contact:create')
  
  if request.method == 'POST':
    form = ContactForm(request.POST, request.FILES)

    context = {
      'form': form,
      'form_action': form_action
    }

    if form.is_valid():
      contact = form.save(commit=False)
      contact.owner = request.user
      contact.save()
      return redirect('contact:update', contact_id=contact.pk)

    return render(
      request,
      'contact/create.html',
      context
    )

  context = {
    'form': ContactForm(),
    'form_action': form_action
  }

  return render(
    request,
    'contact/create.html', 
    context
  )

@login_required(login_url='contact:login')
def update(request, contact_id):
  '''Permite que usuários atualizem um contato existente que possuem. 
  O contato é recuperado e um formulário pré-preenchido com seus dados 
  é apresentado. Após um envio válido do formulário, o contato é atualizado'''
  contact = get_object_or_404(
    Contact, pk=contact_id, show=True, owner=request.user
    )
  form_action = reverse('contact:update', args=(contact_id,))
  
  if request.method == 'POST':
    form = ContactForm(request.POST, request.FILES, instance=contact)

    context = {
      'form': form,
      'form_action': form_action
    }

    if form.is_valid():
      contact = form.save()
      return redirect('contact:update', contact_id=contact.pk)

    return render(
      request,
      'contact/create.html',
      context
    )

  context = {
    'form': ContactForm(instance=contact),
    'form_action': form_action,
  }

  return render(
    request,
    'contact/create.html', 
    context
  )

@login_required(login_url='contact:login')
def delete(request, contact_id):
  '''Fornece funcionalidade para que usuários deletem um contato que possuem. 
  Solicita confirmação antes da exclusão e se confirmado, o contato é deletado 
  e o usuário é redirecionado para a página inicial'''
  contact = get_object_or_404(
    Contact, pk=contact_id, show=True, owner=request.user
    )

  confirmation = request.POST.get('confirmation', 'no')

  if confirmation == 'yes':
    contact.delete()
    return redirect('contact:index')

  return render(
    request,
    'contact/contact.html',
    {
      'contact': contact,
      'confirmation': confirmation,
    }
  )