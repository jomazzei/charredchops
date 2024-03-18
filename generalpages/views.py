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


def custom_404(request, exception):
    """
    Renders custom 404 page
    """
    return render(request, "generalpages/404.html")


def custom_403(request, exception):
    """
    Renders custom 403 page
    """
    return render(request, "generalpages/403.html")


def custom_403_csrf(request, exception):
    """
    Renders custom 403 CSRF request page
    """
    return render(request, "generalpages/403_csrf.html")


def custom_500(request):
    """
    Renders custom 500 page
    """
    return render(request, "generalpages/500.html")

def custom_400(request, exception):
    """
    Renders custom 400 page
    """
    return render(request, "generalpages/400.html")
