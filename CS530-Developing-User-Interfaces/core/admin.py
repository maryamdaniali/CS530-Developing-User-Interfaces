from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.
from core.models import *

admin.site.register(Profile)
admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(Direction)