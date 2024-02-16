import json

def add_report():
  #Cargar archivo
  with open('reportes.json', 'r')as archivo:
    data = json.load(archivo)
  #Logica para agregar usuario 
  new_servi = {
    "name": input("Ingresa nombre del servicio: "),
    "caracteristicas": input("Ingresa caracteristicas del servicio: "),
    "precio": int(input("Ingresa el precio: ")),
  }
  #Guardarlo 
  data.append(new_servi)

  #Persistencia en Json
  with open('reportes.json', 'w')as archivo:
    json.dump(data, archivo) 

def read_servi():
   with open('gestion_servi.json', 'r')as archivo:
    data = json.load(archivo)
  
    return print(data)
