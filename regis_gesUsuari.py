import json

def add_user():
  #Cargar archivo
  with open('regis_gesUsuari.json', 'r')as archivo:
    data = json.load(archivo)
  #Logica para agregar usuario 
  new_useri = {
    "nombre": input("Ingresa tu nombre: "),
    "direccion": input("Ingresa direccion: "),
    "informacion_contacto": int(input("Numero de telefono: ")),
    "categoria": input("Que categoria es: ")
  }
  #Guardarlo 
  data.append(new_useri)

  #Persistencia en Json
  with open('regis_gesUsuari.json', 'w')as archivo:
    json.dump(data, archivo) 

def read_user():
   with open('regis_gesUsuari.json', 'r')as archivo:
    data = json.load(archivo)
  
    return print(data)
   

def update_user():
  #Cargar archivo
  with open('regis_gesUsuari.json', 'r')as archivo:
    data = json.load(archivo)
  #Buscar por Id 
  busca = int(input("Ingresa el número de telefono: "))

  for usuario in busca:
    if usuario.get("informacion_contacto") == busca:
                print("Que deseas actualizar?")
                new = input("1.name "
                            "2.direccion "
                            "3.informacion_contacto "
                            "4.categoria")
                if new == 1:
                   nuevo_name = input("ingresa el nuevo nombre: ")
                   usuario["nombre"] = nuevo_name
                elif new == 2:
                   nuevo_direccion = input("ingresa la nueva direccion:  ")
                   usuario["direccion"] = nuevo_direccion
                elif new == 3:
                   nuevo_contact = input("ingresa nueva info de contacto:  ")
                   usuario["informacion_contacto"] = nuevo_contact
                elif new == 4:
                   nuevo_category = input("ingresa nueva categoria:  ")
                   usuario["categoria"] = nuevo_category

  #Persistencia en Json
  with open('regis_gesUsuari.json', 'w')as archivo:
    json.dump(data, archivo) 

def eliminar(): 
    #Cargar archivo
    with open('regis_gesUsuari.json', 'r')as archivo:
      data = json.load(archivo)
    
    # Solicitar al usuario el ID a eliminar
    id_eliminar = int(input("Ingrese informacion contacto del usuario a eliminar: "))
        
    # Eliminar el registro por su ID
    data = [usuario for usuario in data if usuario.get("informacion_contacto") != id_eliminar]
        
    # Guardar los datos actualizados en el archivo JSON
    with open('registro.json', 'w') as archivo:
        json.dump(data, archivo)

## REGISTRO Y ALMACENAMIENTO DE SERVICIOS POR USER 

def user_servi():
  #Cargar archivo
  with open('history_uer.json', 'r')as archivo:
    data = json.load(archivo)
  #Buscar por Id 
  busca = int(input("Ingresa el número de telefono: "))

  for data in busca:
    if ["informacion_contacto"] == busca:
      print("Actualizar datos")
  #Logica para agregar usuario 
  new_info = {
    "informacion_contacto": int(input("Numero de telefono: ")),
    "categoria": input("Ingresa la categoria: "),
    "servicios": input("Ingresa que servicios: "),
    "visitas": input("Ingresa contacto con el cliente: ")
  }
  #Guardarlo 
  ["usuario"].append(new_info)

  #Persistencia en Json
  with open('history_uer.json', 'w')as archivo:
    json.dump(data, archivo) 

