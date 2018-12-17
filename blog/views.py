from django.shortcuts import render
from django.http import HttpResponse

news = [
    {
        'title': 'My First Post',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'date': '14 December, 2018',
        'author': 'Artem Roy'
    },
    {
        'title': 'My Second Post',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum....',
        'date': '14 December, 2018',
        'author': ''
    }
]

def home(request):
    data = {
        'news': news,
        'title': 'Blog Main Page'
    }
    return render(request, 'blog/home.html', data)

def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'About'})
