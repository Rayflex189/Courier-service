# Generated by Django 5.1.2 on 2024-10-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_shippingdetail_content_shippingdetail_package_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingdetail',
            name='city',
        ),
        migrations.RemoveField(
            model_name='shippingdetail',
            name='content',
        ),
        migrations.RemoveField(
            model_name='shippingdetail',
            name='package_image',
        ),
        migrations.RemoveField(
            model_name='shippingdetail',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='shippingdetail',
            name='recipient_name',
        ),
        migrations.RemoveField(
            model_name='shippingdetail',
            name='serial_image',
        ),
        migrations.RemoveField(
            model_name='shippingdetail',
            name='state',
        ),
        migrations.RemoveField(
            model_name='shippingdetail',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='current_location',
            field=models.CharField(default='Unknown location', max_length=255),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='description',
            field=models.TextField(default='Default content here', max_length=255),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='destination',
            field=models.CharField(default='Unknown Destination', max_length=255),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='parcel_image',
            field=models.ImageField(blank=True, null=True, upload_to='parcel_images/'),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='receiver',
            field=models.CharField(default='Unknown Receiver', max_length=255),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='status',
            field=models.CharField(default='Unknown status', max_length=50),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='tracking_id_image',
            field=models.ImageField(blank=True, null=True, upload_to='tracking_id_images/'),
        ),
        migrations.AlterField(
            model_name='shippingdetail',
            name='address',
            field=models.CharField(default='Unknown addrss', max_length=255),
        ),
    ]