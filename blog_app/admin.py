from django.contrib import admin
from .models import Category,Blog,About,SocialLink,Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=('title','category','author','status','is_featured')
    search_fields=('id','category__category_name','title','status',)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_name','created_at')
    search_fileds=('category_name',)
    
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self,request):
        count = About.objects.all().count()
        if count == 0 :
            return True
        return False 

    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(SocialLink)
admin.site.register(Comment)