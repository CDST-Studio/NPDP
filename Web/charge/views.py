from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post

def index(request):
    posts = Post.objects.all()

    return render(
        request,
        'charge/index.html',
        {
            'orders' : posts
        }
    )

def complete(request):
    return render(
        request,
        'charge/complete.html',
    )

def upload_File(request):
    form = Post()

    form.user_name = request.POST['user_name']
    form.content = request.POST['content']

    try:
        form.image = request.FILES['image']
    except:
        pass

    form.save()

    return redirect('complete.html')
    