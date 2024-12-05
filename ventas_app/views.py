from django.shortcuts import render, redirect
from .models import Venta

# Vista para mostrar las ventas
def inicio_vistaVenta(request):
    lasventas = Venta.objects.all()
    return render(request, "gestionarVenta.html", {"misventas": lasventas})

# Vista para registrar una nueva venta
def registrarVenta(request):
    id_venta = request.POST["txtcodigo"]
    cantidad = request.POST["numingresos"]
    id_cliente = request.POST["numidcliente"]
    id_empleado = request.POST["numidempleado"]
    id_refaccion = request.POST["numidrefaccion"]
    total=request.POST["numtotal"]
    fecha_venta=request.POST["datefecha"]

    guardarVenta = Venta.objects.create(
        id_venta=id_venta,
        cantidad=cantidad,
        id_cliente=id_cliente,
        id_empleado=id_empleado,
        id_refaccion=id_refaccion,
        total=total,
        fecha_venta=fecha_venta
    )  # Guarda el registro

    return redirect("venta")

# Vista para seleccionar una venta y editar
def seleccionarVenta(request, codigo):
    venta = Venta.objects.get(id_venta=codigo)
    fecha_venta=venta.fecha_venta.strftime('%Y-%m-%d')
    return render(request,"editarVenta.html",{"misventas":venta, "misventas" : venta, "fecha_venta" : fecha_venta})

# Vista para editar una venta
def editarVenta(request):
    id_venta = request.POST["txtcodigo"]
    cantidad = request.POST["numingresos"]
    id_cliente = request.POST["numidcliente"]
    id_empleado = request.POST["numidempleado"]
    id_refaccion = request.POST["numidrefaccion"]
    total=request.POST["numtotal"]
    fecha_venta=request.POST["datefecha"]

    venta = Venta.objects.get(id_venta=id_venta)
    venta.cantidad = cantidad
    venta.id_cliente = id_cliente
    venta.id_empleado = id_empleado
    venta.id_refaccion = id_refaccion
    venta.total = total
    venta.fecha_venta = fecha_venta

    venta.save()  # Guarda la venta actualizada
    return redirect("venta")

# Vista para borrar una venta
def borrarVenta(request, codigo):
    venta = Venta.objects.get(id_venta=codigo)
    venta.delete()  # Borra el registro
    return redirect("venta")
