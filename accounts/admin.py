from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'is_staff', 'is_government_employee', 'is_tender_holder')


admin.site.register(User, UserAdmin)
