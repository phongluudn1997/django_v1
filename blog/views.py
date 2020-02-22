from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post comment',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Secode post content',
        'date_posted': 'February 21, 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
