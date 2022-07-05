from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse("<h1>Hello, {} de {} anos!</h1>".format(nome, idade))

def soma(request, num1, num2):
    resultado = num1 + num2
    return HttpResponse("O resultado da soma é {}".format(resultado))