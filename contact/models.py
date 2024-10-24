from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
  '''Define o modelo para armazenar categorias 
  que podem ser associadas a contatos'''
  class Meta:
    '''Define o nome singular e plural do modelo'''
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  name = models.CharField(max_length=50)

  def __str__(self) -> str:
    '''Representa a categoria através de seu nome'''
    return self.name

class Contact(models.Model):
  '''Define o modelo para armazenar informações sobre contatos'''
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50, blank=True)
  phone = models.CharField(max_length=50)
  email = models.EmailField(max_length=250, blank=True)
  created_date = models.DateTimeField(default=timezone.now)
  description = models.TextField(blank=True)
  show = models.BooleanField(default=True)
  picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
  category = models.ForeignKey(
    Category, 
    on_delete=models.SET_NULL, 
    blank=True, null=True
  )
  owner = models.ForeignKey(
    User, 
    on_delete=models.SET_NULL, 
    blank=True, null=True
  )


  def __str__(self) -> str:
    '''Representação textual do contato'''
    return f'{self.first_name} {self.last_name}'