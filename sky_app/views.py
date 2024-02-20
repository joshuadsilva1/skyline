from django.shortcuts import render

# Create your views here.


def sky(request):


    return render(request, 'sky/index.html')




def aboutus(request):


    return render(request, 'sky/aboutus.html')