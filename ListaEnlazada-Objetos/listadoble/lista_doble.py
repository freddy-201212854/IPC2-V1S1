from listadoble.nodo import Nodo
from animal import Animal
import xml.etree.ElementTree as ET

class Lista_Doble:
    def __init__(self):
        self.cabeza = None


    def add(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    
    def Imprimir_LD(self):
        actual = self.cabeza
        actual.dato.imprimir()
        while actual.siguiente is not None:
            actual = actual.siguiente
            actual.dato.imprimir()


    def CargarXML_LD(self, operacion):
        
        tree = ET.parse('animales.xml')
        root = tree.getroot()

        for indice, personas in enumerate(root.findall('persona')):
            codigo = personas.find('codigo').text
            nombre = personas.find('nombre').text
            edad = personas.find('edad').text
            encargado = personas.find('encargado').text
            raza = personas.find('raza').text

            objeto = Animal(codigo, nombre, edad, encargado, raza)
            self.add(objeto)
    """
    def cargar_pelicula(self, lista_doble):
        tree = ET.parse('peliculas.xml')
        root = tree.getroot()

        #cine = root.find('categorias')
        lista_categoria = []
        for categoria in root.findall("categoria"):
            nombre = categoria.find('nombre').text
            print(f"Nombre: {nombre.strip()}")
            pelicula = categoria.find('peliculas')

            for peli in pelicula.findall('pelicula'):
                titulo = peli.find('titulo').text
                director = peli.find('director').text
                anio = peli.find('anio').text
                fecha = peli.find('fecha').text
                hora = peli.find('hora').text
                print(titulo)

                objeto = Pelicula(nombre, titulo, director, anio, fecha, hora)
                
                self.add(objeto)
    """
