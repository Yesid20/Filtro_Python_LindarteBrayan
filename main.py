## ------------------------------------------------------------------
## ---- Filtro ----
## ------------------------------------------------------------------


import clientes_leales as cl
import regis_gesUsuari as rg
import gestion_servi as gs

print("*"*20)
print("Bienvenido a MOVISTAR")
print("*"*20)

name = input("Ingresa tu usuario: ")
print(f"Bienvenido/a {name} como te encuentras hoy?")
print("**** Menu ****")
funcion = int(input("1.Base de datos de usuarios. "
                    "2.Catalogo de servicios. "
                    "3.Salir: " ))
if funcion == 1:
    print("*"*30)
    menu = int(input( "1.Registro y gestion de usuarios. "
                    "2.Seguimiento historial de usuarios. "
                    "3.Personalizacion de servicios. "
                    "4.Gestion de la fidelizacion de clientes. "
                    "5.Salir: "))
    if menu == 1:
      option = int(input("1.Crear usuario. "
                    "2.Ver usuarios. "
                    "3.Actualizar usuarios. "
                    "4.Eliminar usuarios. "
                    "5.Salir: "))
      if option == 1:
        rg.add_user()
      elif option == 2:
        rg.read_user()
      elif option == 3:
        rg.update_user()
      elif option == 4:
        rg.eliminar()
      elif option == 5:
        print("Muchas gracias por utilizar nuestros servicios.")
elif funcion == 2:
    print("*"*30)
    menuu = int(input("1.Crear servicio. "
                    "2.Ver servicios existentes. "
                    "3.Actualizar servicios. "
                    "4.Eliminar servicios. "
                    "5.Salir: "))
    if menuu == 1:
      gs.add_service()
    elif menuu == 2:
      gs.read_servi()
    elif menuu == 3:
      gs.actualizar()
    elif menuu == 4:
      gs.eliminar()
    elif menuu == 5:
      print("Muchas gracias por utilizar nuestros servicios.")
    



else:
   print("Adios, ten buen dia.")


              
