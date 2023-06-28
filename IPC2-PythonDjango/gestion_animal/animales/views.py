from django.shortcuts import redirect, render
from animales.Clases.lista_enlazada import ListaEnlazada
import requests #pip install requests
# Create your views here.
global lista
lista = ListaEnlazada()

global username
def lista_animales(request):
    username = request.session.get('username')
    print(username)
    return render(request, 'animales/lista_animales.html', {'animales': lista})

def cargar_xml(request):
    lista = ListaEnlazada()
    
    if request.method == 'POST':
        lista.CargarXML(1)

        response = requests.get('http://localhost:5007/getAnimales')
        animales_API = response.json()
        print(animales_API)

        for animales in animales_API:
           lista.add(animales)

        response = requests.get('http://localhost:5007/getPeliculas')
        peliculas = response.json()

        for categoria in peliculas['categoria']:
             nombre_categoria = categoria['nombre']
             print("Categoría", nombre_categoria)

             peliculas = categoria['peliculas']['pelicula']
             for pelicula in peliculas:
                 titulo = pelicula['titulo']
                 print("-------", titulo)


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

def inicio_sesion(request):
    print (request.session.get('username'))
    if 'username' in request.session: 
        return render(request, 'animales/lista_animales.html')

    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            request.session['username'] = username
                
            return redirect('lista_animales')
        return render(request, 'animales/inicio_sesion.html')
    
def cerrar_sesion(request):
    if 'username' in request.session:
        request.session.pop('username')
        return redirect('inicio_sesion')
    return redirect('inicio_sesion')
