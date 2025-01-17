from django.contrib import admin

from .models import Complaint, Flat, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ["owner", "flat",]
    extra = 0


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ["id", "town", "address",]
    readonly_fields = ["created_at",]
    list_display = ["id", "town", "address", "price",]
    list_filter = ["new_building", "rooms_number", "floor", "has_balcony",]
    raw_id_fields = ["liked_by",]
    inlines = [OwnerInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["flat",]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "pure_phonenumber",]
    search_fields = ["id", "full_name",]
    inlines = [OwnerInline]
    exclude = ["flat"]
