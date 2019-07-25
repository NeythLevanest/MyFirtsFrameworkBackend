from django.shortcuts import render, redirect
from .forms import RegForm
from .models import Persona
# Create your views here.
def home(request, dato):
    return render(request,"home.html",{'nombre':dato})

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST or None)
        #print(dir(form))
        if form.is_valid():
            form_data=form.cleaned_data
            idPersona = form_data.get("Cédula")
            nombre = form_data.get("Nombre")
            apellido = form_data.get("Apellido")
            edad = form_data.get("Edad")
            fechaNacimiento = form_data.get("Nacimiento")

            objPersona = Persona.objects.create(idPersona=idPersona,
                                            nombre=nombre,
                                            apellido=apellido,
                                            edad=edad,
                                            fechaNacimiento=fechaNacimiento)

            return home(request,objPersona.NombreCompleto())
    else:
        form = RegForm()
    return render(request,"registro.html",{'our_form':form})
