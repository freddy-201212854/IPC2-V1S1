listaPelicula = []

objeto = ("1","Pelicula1", "Joe", "2023-06-05" ,"18:30")
objeto2 = ("2", "Pelicula2", "Joe", "2023-06-05", "19:30")
objeto3 = ("3","Pelicula3", "Joe", "2023-06-05", "20:30")

listaPelicula.append(objeto)
listaPelicula.append(objeto2)
listaPelicula.append(objeto3)

for pelicula in listaPelicula:
    print(f"[{pelicula[0]}.] Titulo {pelicula[1]}")

id_pelicula = input("Ingrese el id de la pelicual:")

titulo = ""
fecha = ""
hora = ""
for pelicula in listaPelicula:
    if id_pelicula == pelicula[0]:
        titulo = pelicula[1]
        fecha = pelicula[2]
        hora = pelicula[3]

n_boleto = input("Ingrese el numero de boletos: ")

#Imprimir el listado de salas
n_sala = input("Ingrese el numero de sala: ")
#Se recorre la lista de salas y se verifica que exista

n_asiento = input("Ingrese el numero de asiento: ")
# Se valida que el numero de asiento este en el rango de la sala

#TOMAR COMO MONTO POR DEFECTO PARA TODAS LAS PELICULAS DE Q 42.00
monto_total = int(n_boleto) * 42

datos_facturacion = input("Desea ingreasar datos de facturacion s/n")

if datos_facturacion.lower() == 's' :
    nit = input("Ingrese el NIT")
    nombre = input("Ingrese el nombre")
    direccion = input("Ingrese la direccion")
    print(f"NIT: {nit}")
    print(f"NIT: {nombre}")
    print(f"NIT: {direccion}")

else:
    print("NIT: CF")

print(f"Monto total a pagar: {monto_total}")

## por ultimo insertar todos los valores de las variables en un objeto e insertarlo en la lista nativa