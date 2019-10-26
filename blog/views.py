from django.shortcuts import render

posts = [
    {
        'author': 'GregJ',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 25, 2019'
    },
    {
        'author': 'zulu',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'October 26, 2019'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})