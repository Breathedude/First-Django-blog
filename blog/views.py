from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
   # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')---error here.
    #return render(request, 'blog/post_list.html', {'posts': posts})
    #Gives no objects for Post!