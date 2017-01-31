from django.shortcuts import render


def index(request):
	return render(request, 'index.html')
	

def transparencia(request):
	return render(request, 'transparencia.html')
