from django.shortcuts import render

# Create your views here.
def BaseKenny(request):
    context = {}
    return render(request, 'app/base.html', context)

def Inicio(request):
    context = {}
    return render(request, 'app/inicio.html',context)