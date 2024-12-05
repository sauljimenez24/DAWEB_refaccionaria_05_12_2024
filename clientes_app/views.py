from django.shortcuts import render, redirect
from .models import Cliente

# Vista para mostrar los clientes
def inicio_vistaCliente(request):
    losclientes = Cliente.objects.all()
    return render(request, "gestionarCliente.html", {"misclientes": losclientes})

# Vista para registrar un nuevo cliente
def registrarCliente(request):
    id_cliente = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    email = request.POST["txtemail"]
    edad = request.POST["numedad"]
    num_cel = request.POST["numcel"]
    sexo = request.POST["txtsexo"]
    direccion = request.POST["txtdireccion"]

    guardarCliente = Cliente.objects.create(
        id_cliente=id_cliente,
        nombre=nombre,
        email=email,
        edad=edad,
        sexo=sexo,
        direccion=direccion,
        num_cel=num_cel
    )  # Guarda el registro

    return redirect("cliente")

# Vista para seleccionar un cliente y editar
def seleccionarCliente(request, codigo):
    cliente = Cliente.objects.get(id_cliente=codigo)
    return render(request, "editarCliente.html", {"misclientes": cliente})

# Vista para editar un cliente
def editarCliente(request):
    id_cliente = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    email = request.POST["txtemail"]
    edad = request.POST["numedad"]
    sexo = request.POST["txtsexo"]
    direccion = request.POST["txtdireccion"]
    num_cel = request.POST["numcel"]
    
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.email = email
    cliente.edad = edad
    cliente.sexo = sexo
    cliente.direccion = direccion
    cliente.num_cel = num_cel
    
    cliente.save()  # Guarda el cliente actualizado
    return redirect("cliente")

# Vista para borrar un cliente
def borrarCliente(request, codigo):
    cliente = Cliente.objects.get(id_cliente=codigo)
    cliente.delete()  # Borra el registro
    return redirect("cliente")
