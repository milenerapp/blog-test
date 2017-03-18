from django.shortcuts import render
def post_list(request):
        return render(request, 'blog/post_list.html',{})
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
# Create your views here.
from django.shortcuts import render
from .models import Post
