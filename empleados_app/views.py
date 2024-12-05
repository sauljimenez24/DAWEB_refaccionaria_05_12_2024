from django.shortcuts import render, redirect
from .models import Empleado

# Vista para mostrar los empleados
def inicio_vistaEmpleado(request):
    losempleados = Empleado.objects.all()
    return render(request, "gestionarEmpleado.html", {"misempleados": losempleados})

# Vista para registrar un nuevo empleado
def registrarEmpleado(request):
    id_empleado = request.POST["txtcodigo"]
    numero_de_cel = request.POST["numcel"]
    fecha_nac = request.POST["txtfechanac"]
    direccion = request.POST["txtdireccion"]
    sexo = request.POST["txtsexo"]
    correo = request.POST["txtcorreo"]

    guardarEmpleado = Empleado.objects.create(
        id_empleado=id_empleado,
        numero_de_cel=numero_de_cel,
        fecha_nac=fecha_nac,
        direccion=direccion,
        sexo=sexo,
        correo=correo
    )  # Guarda el registro

    return redirect("empleado")

# Vista para seleccionar un empleado y editar
def seleccionarEmpleado(request, codigo):
    empleado = Empleado.objects.get(id_empleado=codigo)
    fecha_nac=empleado.fecha_nac.strftime('%Y-%m-%d')
    return render(request,"editarEmpleado.html",{"misempleados":empleado, "misempleados" : empleado, "fecha_nac" : fecha_nac})

# Vista para editar un empleado
def editarEmpleado(request):
    id_empleado = request.POST["txtcodigo"]
    numero_de_cel = request.POST["numcel"]
    fecha_nac = request.POST["txtfechanac"]
    direccion = request.POST["txtdireccion"]
    sexo = request.POST["txtsexo"]
    correo = request.POST["txtcorreo"]

    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.numero_de_cel = numero_de_cel
    empleado.fecha_nac = fecha_nac
    empleado.direccion = direccion
    empleado.sexo = sexo
    empleado.correo = correo

    empleado.save()  # Guarda el empleado actualizado
    return redirect("empleado")

# Vista para borrar un empleado
def borrarEmpleado(request, codigo):
    empleado = Empleado.objects.get(id_empleado=codigo)
    empleado.delete()  # Borra el registro
    return redirect("empleado")
