from django.shortcuts import render, redirect
from .models import Refaccion

# Vista para mostrar las refacciones
def inicio_vistaRefaccion(request):
    lasrefacciones = Refaccion.objects.all()
    return render(request, "gestionarRefaccion.html", {"misrefacciones": lasrefacciones})

# Vista para registrar una nueva refacción
def registrarRefaccion(request):
    id_refaccion = request.POST["txtcodigo"]
    nombre_refaccion = request.POST["txtnombre"]
    cantidad = request.POST["numcantidad"]
    precio = request.POST["numprecio"]
    marca = request.POST["txtmarca"]
    id_provedor = request.POST["numidprov"]

    guardarRefaccion = Refaccion.objects.create(
        id_refaccion=id_refaccion,
        nombre_refaccion=nombre_refaccion,
        cantidad=cantidad,
        precio=precio,
        marca=marca,
        id_provedor=id_provedor
    )  # Guarda el registro

    return redirect("refaccion")

# Vista para seleccionar una refacción y editar
def seleccionarRefaccion(request, codigo):
    refaccion = Refaccion.objects.get(id_refaccion=codigo)
    return render(request, "editarRefaccion.html", {"misrefacciones": refaccion})

# Vista para editar una refacción
def editarRefaccion(request):
    id_refaccion = request.POST["txtcodigo"]
    nombre_refaccion = request.POST["txtnombre"]
    cantidad = request.POST["numcantidad"]
    precio = request.POST["numprecio"]
    marca = request.POST["txtmarca"]
    id_provedor = request.POST["numidprov"]

    refaccion = Refaccion.objects.get(id_refaccion=id_refaccion)
    refaccion.nombre_refaccion = nombre_refaccion
    refaccion.cantidad = cantidad
    refaccion.precio = precio
    refaccion.marca = marca
    refaccion.id_provedor = id_provedor

    refaccion.save()  # Guarda la refacción actualizada
    return redirect("refaccion")

# Vista para borrar una refacción
def borrarRefaccion(request, codigo):
    refaccion = Refaccion.objects.get(id_refaccion=codigo)
    refaccion.delete()  # Borra el registro
    return redirect("refaccion")
