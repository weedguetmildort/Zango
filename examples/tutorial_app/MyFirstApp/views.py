from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Home view
def home(request):
    return render(request, 'home.html')

def custom_400_view(request, exception):
    return render(request, '400.html', {}, status=400)

def custom_403_view(request, exception):
    return render(request, '403.html', {}, status=403)

def custom_404_view(request, exception):
    return render(request, '404.html', {}, status=404)

def custom_500_view(request):
    return render(request, '500.html', {}, status=500)

def custom_502_view(request):
    return render(request, '502.html', {}, status=502)