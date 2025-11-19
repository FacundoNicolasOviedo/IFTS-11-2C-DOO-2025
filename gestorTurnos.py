import clientes
import empleados
import database


def menu():    
     print("Bienvenido a la peluqueria El Viejo Manos de Peine")
     print("Seleccione una opción")
     print("1. Mostrar clientes")
     print("2. Registrar nuevo cliente")
     print("3. Mostrar empleados")
     print("4. Registrar Nuevo empleado")
     print("5. Solicitar turno") 
     print("6. Listar turnos existentes") 
     print("7. Modificar o cancelar turno") 
     print("8. Guardar datos en CSV / Cargar desde dict") 
     print("9. Salir") 
     n = input("Seleccione una opción: ")
     if n == "1":
         db = database.Database("Clientes.csv")
         registros = db.read()
         print(registros)
         menu()
     elif n == "2":
         clientes.Cliente.agregar_a_csv("Clientes.csv")
         menu()
     elif n == "3":
         db = database.Database("Empleados.csv")
         registros = db.read()
         print(registros)
         menu()
     elif n == "4":
         empleados.Empleado.agregar_a_csv("Empleados.csv")
     elif n == "5":
         db = database.Database("Turnos.csv")
         registros = db.read()
         print(registros)
         menu()
     elif n == "9":
         print("Usted ha salido del sistema")
        
        
menu()




