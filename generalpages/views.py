from django.shortcuts import render


# Create your views here.
def home_page(request):
    """
    Renders the home page
    """
    return render(request, "generalpages/home.html")


def menu_page(request):
    """
    Renders the menu page
    """
    return render(request, "generalpages/menu.html")
