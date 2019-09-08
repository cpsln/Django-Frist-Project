from datetime import datetime

from django.shortcuts import render, redirect
from .models import Post
from django.shortcuts import render, get_object_or_404
from .form import PostForm


def post_list(request):
    posts = Post.objects.all()

    for i in posts:
        print(
            '''
                ************
                8           8
                8           8
                *************
            ''', i.published_date, '\n', i.title, '\n', 'id==', i.id
        )

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print('werqr')
    return render(request, 'blog/post_detail.html', {'post': post.pk})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.now()
            # post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.now()
            # post.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
