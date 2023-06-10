from listaDCircular.nodo import Nodo
from animal import Animal
import xml.etree.ElementTree as ET

class listaDobleCircular:
    def __init__(self):
        self.cabeza = None

    def add(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.cabeza is None:
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            ultimo = self.cabeza.anterior

            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = ultimo

            self.cabeza.anterior = nuevo_nodo
            ultimo.siguiente = nuevo_nodo

    
    def Imprimir_LDC(self):
        if self.cabeza is None:
            print("La lista esta vacía")
        
        else:
            nodo_actual = self.cabeza
            while True:
                nodo_actual.dato.imprimir()
                nodo_actual = nodo_actual.siguiente

                if nodo_actual == self.cabeza:
                    break

    def CargarXML_LDC(self):
        
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