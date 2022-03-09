from django.contrib import admin
from django.contrib.auth.admin import UserAdmin,GroupAdmin
from django.contrib.auth.models import User,Group,Permission
from issuerAccounts.models import *
from django.utils.translation import gettext_lazy as _

# Register your models here.
class MyUserAdmin(UserAdmin):
 
    fieldsets = (
        (None, {'fields': ('username','password')}),
        (_('Personal info'), {'fields': ('first_name','last_name','email')}),
        (_('Permissions'), {'fields': ('is_active','is_staff','is_superuser','user_permissions')}),
        (_('Important dates'), {'fields': ('last_login','date_joined')}),
    )
    filter_vertical = ("user_permissions",)

    list_display = ("username","first_name","last_name","email","is_active","is_staff")

class UserAdmin(admin.ModelAdmin):
    list_display =("last_name","email","address","phone","created_date")
    search_fields = ('last_name',)

class ClientAdmin(admin.ModelAdmin):
    list_display =("last_name","email","address","phone","created_date")
    search_fields = ('last_name',)

class InsuranceContractAdmin(admin.ModelAdmin):
    list_display =("user","client","created_at")
    search_fields = ('client__email',)

class PaymentAdmin(admin.ModelAdmin):
    list_display =("contract","user","start_date","end_date","is_approved")
    search_fields = ('contract__client__email',)

class UserInfoAdmin(admin.ModelAdmin):
    list_display =("user","phone","address","date_added")
    search_fields = ('user__username',)

class PermissionAdmin(admin.ModelAdmin):
    list_display =("name","codename")

class ProfileAdmin(admin.ModelAdmin):
    list_display =("user","image","date_updated")
    search_fields = ('user__username',)

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Permission,PermissionAdmin)
admin.site.register(User,MyUserAdmin)
admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(InsuranceContract,InsuranceContractAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Map)

admin.site.site_url = "/homepage_url"
admin.empty_value_display = '**Empty**'
