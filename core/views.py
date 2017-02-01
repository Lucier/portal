from django.shortcuts import render


def index(request):
	return render(request, 'index.html')
	

def transparencia(request):
	return render(request, 'transparencia.html')

def receitas(request):
	return render(request, 'receitas.html')

def despesas(request):
	return render(request, 'despesas.html')
