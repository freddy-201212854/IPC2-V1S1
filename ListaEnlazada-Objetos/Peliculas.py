import xml.etree.ElementTree as ET

tree = ET.parse('peliculas.xml')
root = tree.getroot()

#cine = root.find('categorias')

for categoria in root.findall("categoria"):
    nombre = categoria.find('nombre').text
    print(f"Nombre: {nombre.strip()}")
    pelicula = categoria.find('peliculas')

    for peli in pelicula.findall('pelicula'):
        titulo = peli.find('titulo').text
        print(titulo)


