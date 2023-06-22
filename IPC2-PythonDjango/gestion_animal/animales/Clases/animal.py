class Animal:
    def __init__(self, codigo, nombre, edad, encargado, raza, imagen):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.encargado = encargado
        self.raza = raza
        self.imagen = imagen    

    def imprimir(self):
        #print(self.codigo)
        #print(self.nombre)
        #print(self.edad)
        #print(self.encargado)
        #print(self.raza)

        print(f"Codigo: {self.codigo} Nombre: {self.nombre} Edad: {self.edad} Encargado: {self.encargado} Raza: {self.raza}")