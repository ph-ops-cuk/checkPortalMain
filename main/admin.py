from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Check)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Result)
admin.site.register(Site)