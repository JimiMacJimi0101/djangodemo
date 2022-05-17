from django.shortcuts import render, redirect


def index(request):
    return render(request, 'food/index.html', context=None)

def send(request):
    
    sprava = request.GET["sprava"]
    
    return render(request,'index.html',{'sprava':sprava})
