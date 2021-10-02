from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Order

def index(request):
    orders = Order.objects.all()

    return render(
        request,
        'charge/index.html',
        {
            'orders' : orders
        }
    )