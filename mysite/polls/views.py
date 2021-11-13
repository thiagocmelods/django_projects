from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>First Project in Django</h1><p>Hello, world. You're at the polls index.</p>")