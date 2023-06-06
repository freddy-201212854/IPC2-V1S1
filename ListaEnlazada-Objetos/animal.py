class Animal:
    def __init__(self, codigo, nombre, edad, encargado, raza):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.encargado = encargado
        self.raza = raza

    def imprimir(self):
        #print(self.codigo)
        #print(self.nombre)
        #print(self.edad)
        #print(self.encargado)
        #print(self.raza)

        print(f"Codigo: {self.codigo} Nombre: {self.nombre}")