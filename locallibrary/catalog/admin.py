
from django.contrib import admin
from .models import Book, BookInstance, Genre, Language, Author

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status', 'due_back', 'imprint')  # Fields to display in the list view
    list_filter = ('status', 'due_back')  # Filters in the sidebar

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Author, AuthorAdmin)
