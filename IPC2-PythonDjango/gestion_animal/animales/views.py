from django.shortcuts import redirect, render
# Create your views here.
animales_list = [
    {'codigo': 1, 'nombre': 'Fido', 'edad': 5, 'encargado': 'IPC2', 'raza': 'Chihuahua'},
    {'codigo': 2, 'nombre': 'Firulais', 'edad': 6, 'encargado': 'IPC2', 'raza': 'Desconocida'},
    {'codigo': 3, 'nombre': 'Milo', 'edad': 3, 'encargado': 'IPC2', 'raza': 'Desconocida'},
]


def lista_animales(request):
    return render(request, 'animales/lista_animales.html', {'animales': animales_list})

def crear_animal(request):   
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        encargado = request.POST.get('encargado')
        raza = request.POST.get('raza')

        objeto = {'codigo': codigo, 'nombre': nombre, 'edad': edad, 'encargado': encargado, 'raza': raza}
        animales_list.append(objeto)

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