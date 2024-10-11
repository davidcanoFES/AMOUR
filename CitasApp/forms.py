from django import forms
#from .models import servicios

class Formulario(forms.Form):

    nombre=forms.CharField(label="Nombre(s)*", required=True)
    apellido=forms.CharField(label="Apellido(s)*", required=True)
    telefono=forms.IntegerField(label="Telefono*", required=True)
    correo=forms.EmailField(label="Email", required=True)
    #servicio = forms.ModelChoiceField(queryset=servicios.objects.all(), label="Servicio*", required=True)
    fecha = forms.DateField(widget=forms.SelectDateWidget, label="Fecha*", required=True)
    hora = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label="Hora(HH:MM)*", required=True)

    