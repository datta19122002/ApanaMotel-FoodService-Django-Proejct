from django.contrib import admin
from . models import Person
# Register your models here.
@admin.register(Person)
class Demo(admin.ModelAdmin):
    lists=['first', 'last']
