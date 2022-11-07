from django.shortcuts import render
from .models import Product

# Create your views here.
def homepage(request):
    product = Product.objects.all()
    return render(request = request, template_name="main/home.html", context={'product':product})
