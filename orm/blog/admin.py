from django.contrib import admin
from .models import Blog, Author, Entry


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = 'name', 'tagline'
    search_fields = 'name',
    date_hierarchy = 'entry__pub_date'
   

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = 'name', 'email'
    search_fields = 'name',
    empty_value_display = '-email-'



   
@admin.register(Entry)

class EntryAdmin(admin.ModelAdmin):
        fields = (('headline', 'pub_date', 'number_of_comments'))





    # list_display = 'headline', 'pub_date', 'number_of_comments', 'rating'
    # search_fields = 'headline', 'pub_date', 'rating'
    # list_filter = 'authors', 
   