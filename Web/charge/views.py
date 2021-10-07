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

    #form.content = request.POST['content']

    form.image = request.FILES['image']
    '''try:
        form.image = request.FILES['image']
    except:
        pass'''

    form.save()

    return redirect('complete.html')
    