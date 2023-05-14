from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .models import Post, Category

# Create your views here.
def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug)

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()


    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'blog/detail.html', context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)

    return render(request, 'blog/category.html', {'category': category})