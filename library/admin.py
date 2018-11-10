from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BookInstance,Books
# Register your models here.
admin.site.register(BookInstance)
admin.site.register(Books)

