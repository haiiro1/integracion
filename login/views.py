from django.shortcuts import render

def login(request):
    context = {}
    return render(request, 'crud/login.html',context)

def registro_cliente(request):
    context = {}
    return render(request, 'crud/inicio.html',context)