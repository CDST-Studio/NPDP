from django.shortcuts import render
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

def upload_File(request):
    form = Order()

    form.user_name = request.POST['user_name']
    form.content = request.POST['content']

    try:
        form.image = request.FILES['image']
    except:
        print("씨팔")
        pass

    form.save()

    return redirect('/charge/media')
    