from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, View
from HFSM.models import Post, Signup, slug_generator
from HFSM.forms import ContactForm
from django.contrib import messages


class BlogPageList(ListView):
  model = Post
  template_name = 'blog/blog_list.html'
  paginate_by = 4
  context_object_name = 'posts'


  def get_queryset(self, *args, **kwargs):
    if self.kwargs:
      return Post.objects.filter(status='published').order_by('-time_stamp')
    else:
      query = Post.objects.all().order_by('-time_stamp')
      return query


def detail(request, slug):
    q = Post.objects.filter(slug__iexact = slug)
    if q.exists(): 
        q = q.first()
    else: 
       return render(request, 'errors/404.html', status=404)
  
    context = {
        'post': q
        }
    return render(request, 'blog/blog_detail.html', context) 

def index(request):
    return render(request, 'home.html')

def about(request):
  posts = Post.objects.all()
  template_name = 'about.html'
  form = ContactForm()
  if request.method == 'POST':
    if form.is_valid():
      contact = form(request.POST)
      contact.save()
      return redirect('home')
      messages.success(request, "Thank You We will reply as soon as we can")
    
    else:
      messages.error(request, "Sorry Try Again")
      form = ContactForm()
  else:
    form = ContactForm()
  context = {
    'posts': posts,
    'form': form
  }
  return render(request, template_name, context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
          form.save()
          messages.success(request, "Thank You We will reply as soon as we can")
          return redirect("home")
          
        else:
          messages.error(request, "Sorry Try Again")
          form = ContactForm()
    else:
       form = ContactForm()
    context = {
         'form': form
    }
    return render(request, 'contact.html', context)

