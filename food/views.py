from django.shortcuts import render, redirect


def index(request):
    return render(request, 'food/index.html', context=None)

def pst(request):
    
    sprava = request.POST["sprava"]
    
    return render(request,'index.html',{'sprava':sprava})
