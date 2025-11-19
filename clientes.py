class Cliente(object):
    def __init__(self, nombre, apellido, DNI):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
    
    def agregar_a_csv(nombre_archivo):    
        file = open(nombre_archivo, "at")
        print("Ingresa los datos del nuevo cliente: ")
        Cliente.nombre = input("Ingrese su nombre: ")
        while Cliente.nombre != "":
              Cliente.apellido = input("Ingrese su apellido: ")
              Cliente.DNI = input("ingrese su DNI: ")
              vectorDatabase = [Cliente.nombre, Cliente.apellido, Cliente.DNI]
              fila = ",".join(vectorDatabase) + "\n"
              file.writelines([fila])
              Cliente.nombre = input("Ingrese su nombre: ")
        file.close()