from django.contrib import admin

from .models import Complaint, Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ["town", "address", "owner",]
    readonly_fields = ["created_at",]
    list_display = ["owners_phonenumber", "owner_pure_phone",]
    list_filter = ["new_building", "rooms_number", "floor", "has_balcony",]
    raw_id_fields = ["liked_by",]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["flat",]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)

