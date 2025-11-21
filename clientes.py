from database import Database 

class Cliente(object):
    def __init__(self, nombre, apellido, DNI):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI

    def guardar_en_csv(self, archivo):
        file = open(archivo, "at")
        fila = f"{self.nombre},{self.apellido},{self.DNI}\n"
        file.write(fila)
        file.close()
    
  
    def cargar_clientes_por_consola(archivo):

         
        db = Database(archivo)

        print("Ingresa los datos del nuevo cliente: ")
        while True:
            nombre = input("ingrese su nombre: ")
            if nombre == "":
                print("Elija un nombre valido")
                break
            apellido = input("ingrese su apellido: ")
            DNI = input("ingrese su DNI: ")

            if db.existe_dni(DNI):
                print("El cliente ya se encuentra registrado")

            cliente = Cliente(nombre, apellido, DNI)
            cliente.guardar_en_csv(archivo)
