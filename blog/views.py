from django.shortcuts import render


def index(request):
    """View home page"""

    template = "blog/index.html"
    return render(request, template)
