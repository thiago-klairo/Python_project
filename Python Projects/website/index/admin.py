from operator import index
from django.contrib import admin
from index.models import Fruits, Region

# Register your models here.


class Regions(admin.ModelAdmin):
  @admin.register(Fruits)
  class fruitsAdmin(admin.ModelAdmin):
      list_display = 'name', 'match'    

      

  @admin.register(Region)
  class regionsAdmin(admin.ModelAdmin):
      list_display = 'id', 'name'

 