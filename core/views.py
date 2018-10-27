from django.shortcuts import render, redirect
from .models import Region, Ciudad, Postulante, Vivienda, Raza, Estado, Mascotas
#importamos la mensajeria de django
from django.contrib import messages
#nuevo comentario
from django.contrib.auth.decorators import login_required
#un decorador nos permite agregar funcionalidad a un metodo
# Create your views here.

def home(request):
    return render(request,'core/home.html')


    

#Another solution that worked very well for me and I think it's simplier. It uses OrderedDict() more info
#
#In your views.py file add:
#
#from collections import OrderedDict
#def main(request):
#    ord_dict = OrderedDict()
#    ord_dict['2015-06-20'] = {}
#    ord_dict['2015-06-20']['a'] = '1'
#    ord_dict['2015-06-20']['b'] = '2'
#    ord_dict['2015-06-21'] = {}
#    ord_dict['2015-06-21']['a'] = '10'
#    ord_dict['2015-06-21']['b'] = '20'
#    return render(request, 'main.html', {'context': ord_dict})
#Then in your template, you can do:
#
#<table>
#{% for key, value in context.items %}
#    <tr>
#        <td>{{ key }}</td>
#        <td>{{ value.a }}</td>
#        <td>{{ value.b }} </td>
#    </tr>
#{% endfor %}
#</table>
#This will return the keys of the dictionary in the same ordered that they were put in.
#
#2015-06-20  1   2
#2015-06-21  10  20
#    
def formulario(request):  
    region = Region.objects.all()
    ciudad = Ciudad.objects.all()
    vivienda = Vivienda.objects.all()
    variables = {
        'region':region,
        'ciudad':ciudad,
        'vivienda':vivienda
    }


    if request.POST:
        postulante = Postulante()
        postulante.correo = request.POST.get('txtCorreo')
        postulante.run = request.POST.get('txtRun')
        postulante.nombre = request.POST.get('txtNombre')
        postulante.fecha_nacimiento = request.POST.get("txtFechaNacimiento")
        postulante.telefono = request.POST.get('txtTelefono')
        region = Region()
        region.id = int(request.POST.get('cboRegion'))
        ciudad = Ciudad()
        ciudad.id = int(request.POST.get('cboCiudad'))
        vivienda = Vivienda()
        vivienda.id = int(request.POST.get('cboVivienda'))

        postulante.ciudad = ciudad
        postulante.vivienda = vivienda

        postulante.save()
        try:
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

    return render(request, 'core/formulario.html', variables)










def galeria(request):
    return render(request, 'core/galeria.html')


#CRUD MASCOTA

def formulario_mascota(request):

    estado = Estado.objects.all()
    raza = Raza.objects.all()
    variables = {
        'estado': estado,
        'raza': raza
    }

    if request.POST:
        mascota = Mascotas()
        mascota.nombre = request.POST.get('txtNombreMascota')
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        mascota.raza = raza
        mascota.genero = request.POST.get('txtGenero')
        mascota.fecha_ingreso = request.POST.get('dtFechaIng')
        mascota.fecha_nacimiento = request.POST.get('dtFechaNac')
        mascota.descripcion = request.POST.get('txtDescripcion')
        estado = Estado()
        estado.id = request.POST.get('cboEstado')
        mascota.estado = estado


        try:
            mascota.save()
            variables['mensaje'] = 'Guardado Correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'




    return render(request, 'core/formulario_mascota.html',variables)

#crud de mascotas

def listar_mascota(request):

    mascota = Mascotas.objects.all()


    return render(request, 'core/listar_mascota.html', {
        'mascota':mascota
        
    })



def eliminar_mascota(request, id):
    mascota = Mascotas.objects.get(id=id)
    
    try:
        mascota.delete()
        mensaje = "Eliminado Correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request, mensaje)

    return redirect('listar_mascota')


def modificar_mascota(request, id):
    raza = Raza.objects.all()
    estado = Estado.objects.all()
    mascota = Mascotas.objects.get(id=id) 
    variables = {

        'raza':raza, 
        'estado':estado,
        'mascota':mascota
        
    }

    if request.POST:
        mascota = Mascotas()
        mascota.id = int(request.POST.get("txtId"))
        mascota.nombre = request.POST.get('txtNombreMascota')
        raza = Raza()
        raza.id = int(request.POST.get('cboRaza'))
        mascota.raza = raza
        mascota.genero = request.POST.get('txtGenero')
        mascota.fecha_ingreso = request.POST.get('dtFechaIng')
        mascota.fecha_nacimiento = request.POST.get('dtFechaNac')
        mascota.descripcion = request.POST.get('txtDescripcion')
        estado = Estado()
        estado.id = int(request.POST.get('cboEstado'))
        mascota.estado = estado


        try:
            mascota.save()
            messages.success(request, 'Modificado correctamente')
        except:
            messages.error(request, 'No se ha podido modificar')
        return redirect('listar_mascota')    


    return render(request, 'core/modificar_mascota.html', variables)    