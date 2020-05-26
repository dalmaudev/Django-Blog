from django.shortcuts import render

posts = [
    {
        'author': 'jdalmau',
        'title': 'Blog post numero 1',
        'content': 'Primer contenido en este super blog.',
        'date_posted': '26 de Mayo, 2020',
    },
    {
        'author': 'pepeMarismeño',
        'title': 'Blog post numero 2',
        'content': 'Segundo contenido en este super blog.',
        'date_posted': '23 de Mayo, 2020',
    },
    {
        'author': 'jdalmau33',
        'title': 'Blog post numero 3',
        'content': 'Tercero contenido en este super blog.',
        'date_posted': '22 de Mayo, 2020',
    }
]


def home(request):
    context = {'posts':posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})