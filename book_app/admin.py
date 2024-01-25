from django.contrib import admin
from .models import * #เอามาหมดทุก Class

# Register your models here.
admin.site.register(book_type)
admin.site.register(book_books)
admin.site.register(book_novel)
admin.site.register(book_manga)
admin.site.register(BookType)