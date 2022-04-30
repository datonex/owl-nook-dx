from django.shortcuts import render


def index(request):
    """View home page"""

    template = "blog/blog.html"
    return render(request, template)
