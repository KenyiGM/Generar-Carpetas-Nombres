""" 

Autor : Kenyi Alexander Galindo Martinez

"""
from os import mkdir

with open('lista.txt') as file:
  lista_de_nombres = file.readlines()
  for nombre in lista_de_nombres:
    try:
      if nombre.find("\n") != -1:
        nombre = nombre[:nombre.find("\n")]
      mkdir(nombre)
    except:
      print(f"Ya esta creada la carpeta {nombre}")

file.close()
