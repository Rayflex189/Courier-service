from django.db import models

class ShippingDetail(models.Model):
    code = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=50, default='Unknown status')
    receiver = models.CharField(max_length=255, default='Unknown Receiver')
    address = models.CharField(max_length=255, default='Unknown addrss')
    description = models.TextField(max_length=255, default="Default content here")
    current_location = models.CharField(max_length=255, default='Unknown location')
    tracking_id_image = models.ImageField(upload_to='tracking_id_images/', null=True, blank=True)
    parcel_image = models.ImageField(upload_to='parcel_images/', null=True, blank=True)
    destination = models.CharField(max_length=255, default='Unknown Destination')


    def __str__(self):
        return self.code
