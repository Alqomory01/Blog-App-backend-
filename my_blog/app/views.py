from django.shortcuts import render

def home(request):
    return render(request, 'blog.html')
# Create your views here.
