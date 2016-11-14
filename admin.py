from django.contrib import admin

from .models import Picture,Friend

# Register your models here.

# class UserAdmin(admin.ModelAdmin):
# 	class Meta:
# 		model = User

# class PictureAdmin(admin.ModelAdmin):
# 	class Meta:
# 		model = Picture

admin.site.register(Picture)
admin.site.register(Friend)#, PictureAdmin)
