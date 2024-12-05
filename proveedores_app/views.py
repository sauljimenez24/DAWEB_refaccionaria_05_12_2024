from django.shortcuts import render, redirect
from .models import Proveedor

# Vista para mostrar los proveedores
def inicio_vistaProveedor(request):
    losproveedores = Proveedor.objects.all()
    return render(request, "gestionarProveedor.html", {"misproveedores": losproveedores})

# Vista para registrar un nuevo proveedor
def registrarProveedor(request):
    id_proveedor = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    correo = request.POST["txtcorreo"]
    telefono = request.POST["numtelefono"]
    direccion = request.POST["txtdireccion"]

    guardarProveedor = Proveedor.objects.create(
        id_proveedor=id_proveedor,
        nombre=nombre,
        correo=correo,
        telefono=telefono,
        direccion=direccion
    )  # Guarda el registro

    return redirect("proveedor")

# Vista para seleccionar un proveedor y editar
def seleccionarProveedor(request, codigo):
    proveedor = Proveedor.objects.get(id_proveedor=codigo)
    return render(request, "editarProveedor.html", {"misproveedores": proveedor})

# Vista para editar un proveedor
def editarProveedor(request):
    id_proveedor = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    correo = request.POST["txtcorreo"]
    telefono = request.POST["numtelefono"]
    direccion = request.POST["txtdireccion"]

    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.nombre = nombre
    proveedor.correo = correo
    proveedor.telefono = telefono
    proveedor.direccion = direccion

    proveedor.save()  # Guarda el proveedor actualizado
    return redirect("proveedor")

# Vista para borrar un proveedor
def borrarProveedor(request, codigo):
    proveedor = Proveedor.objects.get(id_proveedor=codigo)
    proveedor.delete()  # Borra el registro
    return redirect("proveedor")
