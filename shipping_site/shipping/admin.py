from django.contrib import admin
from .models import ShippingDetail

@admin.register(ShippingDetail)
class ShippingDetailAdmin(admin.ModelAdmin):
    list_display = ('code', 'status', 'receiver', 'address', 'description', 'current_location', 'tracking_id_image', 'parcel_image', 'destination')
    
    fieldsets = (
        (None, {
            'fields': ('code', 'status')
        }),
        ('Recipient Information', {
            'fields': ('receiver', 'address', 'description', 'current_location', 'tracking_id_image', 'parcel_image', 'destination')
        }),
    )
