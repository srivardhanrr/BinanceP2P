from django.contrib import admin
from .models import *


@admin.register(Contacts)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Pg)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Subscribe)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("email",)


@admin.register(Testimonials)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ServiceInfo)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("happy_clients",)


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "gender", "created_at", "checked")


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("name",)