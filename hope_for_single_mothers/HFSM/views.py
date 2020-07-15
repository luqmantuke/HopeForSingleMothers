from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')
