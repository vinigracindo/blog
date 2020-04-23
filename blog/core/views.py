from django.shortcuts import render
from django.views.generic import DetailView
from django.core.paginator import Paginator
from blog.core.models import Post


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})


class PostDetailView(DetailView):
    model = Post
