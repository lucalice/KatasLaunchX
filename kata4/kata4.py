from pydoc import TextRepr


text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

#Ejercicio 1
text = text.split(". ")
print(text)

words = ["average", "temperature", "distance"]

print(len(text))
for i in text:
    for j in words:
        if j in i:
            print(text)

for i in text:
    for j in words:
        if j in i:
            print(i.replace(" C", " Celsius"))

#Ejercicio 2

# Datos con los que vamos a trabajar
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

# Creamos el título
title = "datos de gravedad sobre "+name

#Plantilla
hechos = f"""{'-'*80} 
Nombre del planeta: {planet} 
Gravedad en {name}: {gravity * 1000} m/s2 
"""

plantilla = f"""{title.title()} 
{hechos} 
""" 
print(hechos)

planet = 'Marte '
gravity  = 0.00143
name = 'Ganímedes'

print(plantilla)

nueva_plantilla = """
Datos de Gravedad sobre: {name}
-------------------------------------------------------------------------------
Nombre del planeta: {planet}
Gravedad en {name}: {gravity} m/s2
"""
print(nueva_plantilla.format(name=name, planet=planet, gravity=gravity))

# Pista: print(nueva_plantilla.format(variables))
print(nueva_plantilla.format(name=name, planet=planet, gravity=gravity*1000))