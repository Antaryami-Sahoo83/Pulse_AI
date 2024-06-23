from django.contrib import admin # type: ignore

from blog.models import BlogCategory, Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
      list_display = ('title', 'category', 'created_at', 'publish')
      search_fields = ('title', 'content')
      list_filter = ('category', 'publish' )
      list_editable = ('publish', )
      # list_per_page = 1
      # summernote_fields = ('content', )

admin.site.register(BlogCategory)
admin.site.register(Blog, BlogAdmin)
