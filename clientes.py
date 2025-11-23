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

        print("Ingresa los datos del nuevo cliente: ")
        while True:
            DNI = input("ingrese su DNI: ")
            if DNI == "":
                print("Elija un DNI valido")
                break
            nombre = input("ingrese su nombre: ")
            if nombre == "":
                print("Elija un nombre valido")
                break
            apellido = input("ingrese su apellido: ")
            if apellido == "":
                print("Elija un apellido valido")
                break
            
            cliente = Cliente(nombre, apellido, DNI)
            cliente.guardar_en_csv(archivo)
