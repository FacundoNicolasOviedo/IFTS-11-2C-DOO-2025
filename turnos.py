import database
import clientes

def solicitar_turno():
   
    db_disponibles = database.Database("Turnos_Disponibles.csv")
    disponibles = db_disponibles.read()  

    
    db_asignados = database.Database("Turnos_Asignados.csv")
    db_asignados.read()  

    
    if not disponibles:
        print("\nNo hay turnos disponibles.")
        return

    print("\nRecordá que solo podrás sacar un turno")
    print("\nTURNOS DISPONIBLES:")
    for s in disponibles:
        print(f"{s['turno_id']} - {s['trabajo']} con {s['profesional']} el {s['dia']} a las {s['hora']}")

 
    turno_id = input("\nElegí una opción: ")

   
    turno_elegido = None
    for s in disponibles:
        if s["turno_id"] == turno_id:
            turno_elegido = s
            break

    if turno_elegido is None:
        print("Elegí un turno válido.")
        return

   
    dni = input("DNI del cliente: ")

    if not clientes.Cliente.dni_existe(dni):
        print("El cliente aún no se encuentra registrado en nuestra base de datos")
    else:
         nueva_lista = [s for s in disponibles if s["turno_id"] != turno_id]

         file = open("Turnos_Disponibles.csv", "wt")
         file.write("turno_id,trabajo,profesional,dia,hora\n")
         for t in nueva_lista:
             linea = ",".join([t["turno_id"], t["trabajo"], t["profesional"], t["dia"], t["hora"]])
             file.write(linea + "\n")
         file.close()

   
         file = open("Turnos_Asignados.csv", "at")
         linea = ",".join([dni, turno_elegido["trabajo"], turno_elegido["profesional"],turno_elegido["dia"], turno_elegido["hora"]])
         file.write(linea + "\n")
         file.close()

         print("\nTurno reservado correctamente\n")

def eliminar_turno():

    db_asig = database.Database("Turnos_Asignados.csv")
    asignados = db_asig.read()

    if not asignados:
        print("No hay turnos asignados.")
        return

   
    print("\nTURNOS ASIGNADOS:")
    for s in asignados:
        print(f"{s['DNI']} - {s['trabajo']} con {s['profesional']} el {s['dia']} a las {s['hora']}")

    
    dni = input("\nIngrese el DNI del turno que desea eliminar: ")

    
    nueva_lista = [s for s in asignados if s["DNI"] != dni]

    
    file = open("Turnos_Asignados.csv", "wt")
    file.write("DNI,trabajo,profesional,dia,hora\n")
    for t in nueva_lista:
        linea = ",".join([t["DNI"], t["trabajo"], t["profesional"], t["dia"], t["hora"]])
        file.write(linea + "\n")
    file.close()

    print("\nTurno eliminado correctamente.\n")