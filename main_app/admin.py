from django.contrib import admin
from .models import Film, Rating, Favorite


# Register your models here.
admin.site.register(Film)
admin.site.register(Rating)
admin.site.register(Favorite)

