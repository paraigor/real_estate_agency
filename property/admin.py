from django.contrib import admin

from .models import Complaint, Flat, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ["id",]
    readonly_fields = ["created_at",]
    list_display = ["id", "town", "address"]
    list_filter = ["new_building", "rooms_number", "floor", "has_balcony",]
    raw_id_fields = ["liked_by",]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["flat",]

class OwnerAdmin(admin.ModelAdmin):
    search_fields = ["full_name",]
    raw_id_fields = ["flat",]

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
