from animales.Clases.nodo import Nodo
from animales.Clases.animal import Animal
import xml.etree.ElementTree as ET

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def add(self, dato):
        
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def modify(self, dato_nuevo, index):
        actual = self.cabeza
        indice = 0

        while actual is not None:
            if indice == index:
                actual.dato = dato_nuevo
                return
            indice += 1
            actual = actual.siguiente

    def Imprimir(self):
        actual = self.cabeza
        #print(actual.dato)
        actual.dato.imprimir()
        while actual.siguiente is not None:
            actual = actual.siguiente
            actual.dato.imprimir()
            #print(actual.dato)

    def loop(self):
        actual = self.cabeza
       
        while actual:
            yield actual.dato
            actual = actual.siguiente


    def __iter__(self):
        return iter(self.loop())

    def CargarXML(self, operacion):
        
        tree = ET.parse('animales.xml')
        root = tree.getroot()

        for indice, personas in enumerate(root.findall('persona')):
            codigo = personas.find('codigo').text
            nombre = personas.find('nombre').text
            edad = personas.find('edad').text
            encargado = personas.find('encargado').text
            raza = personas.find('raza').text
            imagen = personas.find('imagen').text
            objeto = Animal(codigo, nombre, edad, encargado, raza, imagen)
            
            if operacion == 1: # agregar datos a lista
                self.add(objeto)
            elif operacion == 2:
                self.modify(objeto, indice)

            #print(f"codigo: {codigo} nombre: {nombre}")

    def editarXML(self):
        tree = ET.parse('animales.xml')
        root = tree.getroot()

        nombre1 = root.find("persona[1]/nombre")
        nombre1.text = "Fido"

        tree.write("animales.xml")

        self.CargarXML(2)


    def nuevo_registroXML(self):
        tree = ET.parse('animales.xml')
        root = tree.getroot()

        nueva_persona = ET.Element("persona")

        codigo = ET.SubElement(nueva_persona, 'codigo')
        codigo.text = '4'

        nombre = ET.SubElement(nueva_persona, 'nombre')
        nombre.text = "Nuevo dato"

        edad = ET.SubElement(nueva_persona, 'edad')
        edad.text = '40'

        encargado = ET.SubElement(nueva_persona, 'encargado')
        encargado.text = 'Sarai'

        raza = ET.SubElement(nueva_persona, 'raza')
        raza.text = 'Bulldog'

        imagen = ET.SubElement(nueva_persona, 'imagen')
        imagen.text = 'image.png'

        objeto = Animal(codigo.text, nombre.text, edad.text, encargado.text, raza.text, imagen.text)
        self.add(objeto)

        root.append(nueva_persona)

        tree.write('animales.xml')

