from django.shortcuts import render, redirect

from .forms import Formulario
#from .models import clientes, citas as CitasModelo

# Create your views here.

def citas_view(request):
    formulario_contacto=Formulario()

    if request.method=="POST":
        formulario_contacto=Formulario(request.POST)
        if formulario_contacto.is_valid():
            nombre = formulario_contacto.cleaned_data['nombre']
            apellido = formulario_contacto.cleaned_data['apellido']
            telefono = formulario_contacto.cleaned_data['telefono']
            correo = formulario_contacto.cleaned_data['correo']
            servicio = formulario_contacto.cleaned_data['servicio']
            fecha = formulario_contacto.cleaned_data['fecha']
            hora = formulario_contacto.cleaned_data['hora']

      #  try:
         #   cliente, created = clientes.objects.get_or_create(
        #        nombre=nombre,
         #       apellido=apellido,
          #      defaults={'telefono': telefono, 'correo': correo}
        #    )

            # Crear la cita y asociarla al cliente
          #  cita = CitasModelo.objects.create(
        #        cliente=cliente,
        #        fecha=fecha,
       #         hora=hora
           # )

            # Asociar el servicio a la cita
          #  cita.servicios.add(servicio)
         #   return redirect("/citas/?aceptado")
       # except:
      #      return redirect("/citas/?error")
                
            
            
                


            
    return render(request, "CitasApp/registro.html", {'miformulario':formulario_contacto})