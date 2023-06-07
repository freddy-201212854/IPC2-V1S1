from animal import Animal        
from lista_enlazada import ListaEnlazada
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
print("Cargando XML ...")
lista.CargarXML(1)

lista.Imprimir()

print("Editando XML ...")
lista.editarXML()
lista.Imprimir()





    


