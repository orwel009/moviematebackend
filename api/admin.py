from django.contrib import admin
from .models import Movie, AdminMovie
# Register your models here.


admin.site.register(Movie)

@admin.register(AdminMovie)
class AdminMovieAdmin(admin.ModelAdmin):
    list_display = ('title','media_type','platform','genre','created_at')
    search_fields = ('title','director','genre','platform')