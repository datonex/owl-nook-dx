from multiprocessing import context
from .models import Category


def get_categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
        context = {"categories": categories}
        return context
