from django.shortcuts import render

# Create your views here.

def chart(request):
    return render(request,'chart.html')