from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(category_list)
admin.site.register(English_Domain)
admin.site.register(language_list)
admin.site.register(URL_dashboard)
admin.site.register(BulkEmail)
admin.site.register(BulkEmailAttachments)


# Below Modules are for User and Blog related     
admin.site.register(UserProfile)
admin.site.register(UserRole)
admin.site.register(UserRoleMapping)
admin.site.register(CustomForgotPassword)
admin.site.register(OTP_For_UserRegistration)
admin.site.register(BlogCategory)

@admin.register(Blog)
class AdminDocumentWithoutTrans(admin.ModelAdmin):
    list_display = ('id', 'Blog_Title', 'Blog_CreationDate', 'Blog_CategoryType', 'Blog_PublishedStatus', 'Blog_Author')
    list_display_links = ('id', 'Blog_Title')
    list_filter = ('Blog_Title', 'Blog_CreationDate', 'Blog_CategoryType', 'Blog_PublishedStatus', 'Blog_Author')
    search_fields = ('Blog_Title', 'Blog_Author')
    ordering = ('id',)
    list_per_page: int = 20