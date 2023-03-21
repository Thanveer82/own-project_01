from django.shortcuts import render

# Create your views here.
def f(request):
    return render(request,'f.html')

def s(request):
    return render(request,'s.html')

def t(request):
    return render(request,'t.html')

def fo(request):
    return render(request,'fo.html')
