import xml.etree.ElementTree as ET

ruta = input("Ingrese la ruta del archivo xml: ")
tree = ET.parse(ruta)

#tree = ET.parse('C:/Users/vn55nks/Desktop/usuarios.xml')
#tree = ET.parse('C:\\Users\\vn55nks\\Desktop\\usuarios.xml')

root = tree.getroot()

for indice, personas in enumerate(root.findall('usuario')):
    correo = personas.find('correo').text
    print(correo)
    """nombre = personas.find('nombre').text
    edad = personas.find('edad').text
    encargado = personas.find('encargado').text
    raza = personas.find('raza').text"""