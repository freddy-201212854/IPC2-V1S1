from animal import Animal        
from lista_enlazada import ListaEnlazada
from listadoble.lista_doble import Lista_Doble
from listaDCircular.lista_d_circular import listaDobleCircular

objeto = Animal(2023, "Firulais", 5, "Pablo", "Desconocida")
objeto2 = Animal(2024, "Fido", 5, "Pablo", "Chihuahua")

#lista = []
#lista.append(objeto)
#lista.append(objeto2)

#for list in lista:
 #   list.imprimir()

lista = ListaEnlazada()

#lista.add(objeto)
#lista.add(objeto2)

#lista.Imprimir()
print("Cargando XML para lista enlazada ...")
lista.CargarXML(1)

lista.Imprimir()

print("Editando XML para lista enlazada ...")
lista.editarXML()
lista.Imprimir()

print("----------------------------------")
print("----------------------------------")

lista_doble = Lista_Doble()

print("Cargando XML para lista doble...")
lista_doble.CargarXML_LD(1)

lista_doble.Imprimir_LD()

print("----------------------------------")
print("----------------------------------")
print("Agregando nuevo registro a XML ...")
lista.nuevo_registroXML()

lista.Imprimir()

print("----------------------------------")
print("----------------------------------")
lista_dobleC = listaDobleCircular()

print("Cargando XML para lista doble circular...")
lista_dobleC.CargarXML_LDC()

lista_dobleC.Imprimir_LDC()

print("----------------------------------")
print("----------------------------------")





    


