import xml.etree.ElementTree as ET

tree = ET.parse('salas.xml')
root = tree.getroot()

cine = root.find('cine')

for sala in cine.findall("salas/sala"):
    numero = sala.find('numero').text
    asientos = sala.find('asientos').text

    print(f"Numero de sala: {numero.strip()} Asientos: {asientos.strip()}")


"""
print("Ejecutando xml")
for cines in root.findall('cine'):
    salas = cines.find('salas')
    for sala in salas.findall('sala'):
        numero = sala.find('numero').text
        asientos = sala.find('asientos').text

        print(f"Numero de sala: {numero} Asientos: {asientos}")
"""

