from django.contrib import admin
from .models import blog_table,comments

admin.site.register(blog_table)
admin.site.register(comments)
