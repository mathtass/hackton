from django.shortcuts import render
from .models import Formulario

def formulario(request):
    if request.method=='POST':
        usuario = request.POST['usuario']
        assunto = request.POST['assunto']
        descricao = request.POST['descricao']
        data = request.POST['data']
        numero = request.POST['numero']
        numero_reclamacao = request.POST['numero_reclamacao']
        status = request.POST['status']
        anexo = request.POST['anexo']

    return render(request, 'nanotech/formulario.html', {})

def lista_incidentes(request):
    incidentes = Formulario.objects.all().order_by('usuario')
    return render(request, 'nanotech/incidentes.html', {'incidentes':incidentes})