from django.contrib import admin
from .models import Category,Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=('title','category','author','status','is_featured')
    search_fields=('id','category__category_name','title','status',)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_name','created_at')
    search_fileds=('category_name',)
    

admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)