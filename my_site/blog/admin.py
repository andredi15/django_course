from django.contrib import admin
from .models import Post, Author, Tag, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tag", "date") #these need to be the same field names as in the Model. This allows us to apply a filter to posts.
    list_display = ("title", "author", "date") #this is to add columns to the admin panel showing these values.

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")
    
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)

