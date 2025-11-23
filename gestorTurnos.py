import clientes
import empleados
import database
import turnos


def menu():    
     print("Bienvenido a la peluqueria El Viejo Manos de Peine")
     print("Seleccione una opción")
     print("1. Mostrar clientes")
     print("2. Registrar nuevo cliente")
     print("3. Mostrar empleados")
     print("4. Registrar Nuevo empleado")
     print("5. Solicitar turno") 
     print("6. Listar turnos existentes") 
     print("7. Cancelar turno") 
     print("8. Salir") 
     n = input("Seleccione una opción: ")
     if n == "1":
         db = database.Database("Clientes.csv")
         registros = db.read()
         print("\nNUESTROS CLIENTES:\n")
         for s in registros:
             print(f"{s['nombre']} - {s['apellido']} - {s['DNI']}")
         print("\n")
         menu()
     elif n == "2":
         clientes.Cliente.cargar_clientes_por_consola("Clientes.csv")
         menu()
     elif n == "3":
         db = database.Database("Empleados.csv")
         print("\nNUESTROS EMPLEADOS:\n")
         registros = db.read()
         for s in registros:
             print(f"{s['nombre']} - {s['apellido']} - {s['DNI']} - {s['dias']} - {s['horarios']}")
         print("\n")
         menu()
     elif n == "4":
         empleados.Empleado.cargar_empleados_por_consola("Empleados.csv")
     elif n == "5":
         turnos.solicitar_turno()
     elif n == "6":
         db = database.Database("Turnos_Asignados.csv")
         registros = db.read()
         for s in registros:
             print(f"{s['DNI']} - {s['trabajo']} - {s['profesional']} - {s['dia']} - {s['hora']}")
         menu()
     elif n == "7":
         turnos.eliminar_turno()
     elif n == "8":
         print("Usted ha salido del sistema")
        
        
menu()




