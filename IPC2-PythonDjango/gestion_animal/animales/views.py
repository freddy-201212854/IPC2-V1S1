from django.shortcuts import redirect, render
from animales.Clases.lista_enlazada import ListaEnlazada

# Create your views here.
global lista
lista = ListaEnlazada()


def lista_animales(request):
    return render(request, 'animales/lista_animales.html', {'animales': lista})

def cargar_xml(request):
    lista = ListaEnlazada()
    
    if request.method == 'POST':
        lista.CargarXML(1)
    return render(request, 'animales/lista_animales.html', {'animales': lista})

def crear_animal(request):   
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        encargado = request.POST.get('encargado')
        raza = request.POST.get('raza')
        imagen = request.POST.get('imagen')

        objeto = {'codigo': codigo, 'nombre': nombre, 'edad': edad, 'encargado': encargado, 'raza': raza, 'imagen': imagen}
        lista.add(objeto)

        return redirect('lista_animales')
    return render(request, 'animales/crear_animal.html')

def actualizar_animal(request, codigo):
    animal = next((animal for animal in animales_list if animal['codigo'] == codigo), None)
    if animal:
        if request.method == 'POST':
            animal['nombre'] = request.POST.get('nombre')
            animal['encargado'] = request.POST.get('encargado')
            animal['raza'] = request.POST.get('raza')
            return redirect('lista_animales')
        return render(request, 'animales/actualizar_animal.html', {'animal': animal})
    return redirect('lista_animales')

def eliminar_animal(request, codigo):
    animal = next((animal for animal in animales_list if animal['codigo'] == codigo), None)
    if animal:
        animales_list.remove(animal)
    return redirect('lista_animales')