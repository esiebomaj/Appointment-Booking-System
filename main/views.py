from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'main/landing_page.html', {})
