from django.shortcuts import render, get_object_or_404
from .models import ShippingDetail
from django.contrib import messages
# from django.contrib.auth.decorators import login_required  # Uncomment if using login_required

def index(request):
    return render(request, 'shipping/index.html')

def about(request):
    return render(request, 'shipping/about.html')

def service(request):
    return render(request, 'shipping/service.html')

def contact(request):
    return render(request, 'shipping/contact.html')

def feature(request):
    return render(request, 'shipping/feature.html')

def price(request):
    return render(request, 'shipping/price.html')

def qoute(request):  # Corrected function name
    return render(request, 'shipping/qoute.html')

def team(request):
    return render(request, 'shipping/team.html')

def testimonial(request):
    return render(request, 'shipping/testimonial.html')

def custom_404_view(request, exception):
    return render(request, '404.html', {'error_type': '404'}, status=404)

def custom_500_view(request):
    return render(request, '500.html', {'error_type': '500'}, status=500)  # Changed template

# @login_required  # Uncomment if needed
def dashboard(request):
    shipping_detail = None
    error_message = None

    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            shipping_detail = ShippingDetail.objects.get(code=code)
            messages.success(request, "Shipping detail retrieved successfully!")  # Success message
        except ShippingDetail.DoesNotExist:
            error_message = "Shipping code does not exist. Please check and try again."

    return render(request, 'shipping/dashboard.html', {'shipping_detail': shipping_detail, 'error_message': error_message})