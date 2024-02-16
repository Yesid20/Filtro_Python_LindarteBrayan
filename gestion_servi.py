import json

def add_service():
  #Cargar archivo
  with open('gestion_servi.json', 'r')as archivo:
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
  with open('gestion_servi.json', 'w')as archivo:
    json.dump(data, archivo) 

def read_servi():
   with open('gestion_servi.json', 'r')as archivo:
    data = json.load(archivo)
  
    return print(data)

def update_servi():
    with open('gestion_servi.json', 'r') as archivo:
        data = json.load(archivo)

        buscar = int(input("Buscar por precio: "))

        for servicio in data:
            if servicio.get("precio") == buscar:
                print("Que deseas actualizar?")
                new = input("1.name "
                            "2.caracteristicas "
                            "3.precio "
                            "4.salir ")
                if new == 1:
                   nuevo_name = input("ingresa el nuevo nombre: ")
                   servicio["nombre"] = nuevo_name
                if new == 2:
                   nuevo_caract = input("ingresa las nuevas caracteristicas: ")
                   servicio["caracteristicas"] = nuevo_caract
                if new == 3:
                   nuevo_precio = input("ingresa el nuevo precio: ")
                   servicio["nombre"] = nuevo_precio
                if new == 4:
                   print("Muchas gracias por utilizar nuestros servicios.")

    with open('gestion_servi.json', 'w') as archivo:
        json.dump(data, archivo)

def delete_servi(): 
    #Cargar archivo
    with open('gestion_servi.json', 'r')as archivo:
      data = json.load(archivo)
    
    # Solicitar al usuario el ID a eliminar
    precio_eliminar = int(input("Ingrese precio del servicio a eliminar: "))
        
    # Eliminar el registro por su ID
    data = [servicio for servicio in data if servicio.get("precio") != precio_eliminar]
        
    # Guardar los datos actualizados en el archivo JSON
    with open('gestion_servi.json', 'w') as archivo:
        json.dump(data, archivo)
