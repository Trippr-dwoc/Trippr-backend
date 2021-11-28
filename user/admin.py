from django.contrib import admin
from .models import UserProfile, Relation

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','username','email')
    list_display_links = ('id','username')

# Register your models here.
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Relation)