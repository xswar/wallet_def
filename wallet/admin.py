from django.contrib import admin
from .models import Account, Tag, Category, Transaction, Image


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'balance')
    list_display_links = ('id', 'owner')
    list_filter = ('owner',)
    list_editable = ('balance',)
    search_fields = ('name',)
    readonly_fields = ('id',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 1


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_filter = ('account', 'date', 'category', 'tags', 'description', 'amount')
    search_fields = ('account', 'date', 'category', 'tags', 'description', 'amount')
    list_per_page = 1


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'transaction')
