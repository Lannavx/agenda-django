from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
  '''Configura a interface de administração, 
  definindo a exibição, ordenação, busca e paginação dos contatos'''
  list_display = 'id', 'first_name', 'last_name', 'phone',
  ordering = '-id',
  search_fields = 'id', 'first_name', 'last_name',
  list_per_page = 10
  list_max_show_all = 100
  list_display_links = 'id', 'phone',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  '''Configura a interface de administração para o modelo Category, 
  permitindo ordenar e visualizar as categorias'''
  list_display = 'name',
  ordering = '-id',