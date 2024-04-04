from django.contrib import admin

from .models import Action, Incoming

admin.site.register(Incoming)
admin.site.register(Action)
