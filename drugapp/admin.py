from django.contrib import admin
from drugapp.models import State, Prescriber, Drug, Triple

# Register your models here.
admin.site.register(State)
admin.site.register(Prescriber)
admin.site.register(Drug)
admin.site.register(Triple)