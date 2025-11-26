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

    def validar_dni(dni):
         file = open("Clientes.csv", "rt")
         existe = dni in file.read()  
         file.close()
         return existe
  
    def registrar_cliente(archivo):

        print("Ingresa los datos del nuevo cliente: ")
        while True:
            DNI = input("ingrese su DNI: ")
            if DNI == "":
                print("Elija un DNI valido")
                break
            if Cliente.validar_dni(DNI):
                print("El DNI ya se encuentra registrado")
                break
            nombre = input("ingrese su nombre: ")
            if nombre == "":
                print("Elija un nombre valido")
                break
            apellido = input("ingrese su apellido: ")
            if apellido == "":
                print("Elija un apellido valido")
                break
            print("\nCliente registrado con exito\n")
            print("Ingresa los datos del nuevo cliente: ")
            cliente = Cliente(nombre, apellido, DNI)
            cliente.guardar_en_csv(archivo)
