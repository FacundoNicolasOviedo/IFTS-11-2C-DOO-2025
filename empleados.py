class Empleado(object):

    def __init__(self, nombre, apellido, DNI, dias, horarios):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.dias = dias
        self.horarios = horarios
    
    def guardar_en_csv(self, archivo):
        file = open(archivo, "at")
        fila = f"{self.nombre},{self.apellido},{self.DNI}, {self.dias}, {self.horarios}\n"
        file.write(fila)
        file.close()
    
    def validar_dni(dni):
         file = open("Empleados.csv", "rt")
         existe = dni in file.read()  
         file.close()
         return existe

 
    def registrar_empleado(archivo):
        print("Ingresa los datos del nuevo empleado: ")
        while True:
            DNI = input("ingrese su DNI: ")
            if DNI == "":
                print("Elija un DNI valido")
                break
            if Empleado.validar_dni(DNI):
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
            dias = input("ingrese su dias: ")
            if dias == "":
                print("Elija un día valido")
                break
            horarios = input("ingrese su horario: ")
            if horarios == "":
                print("Elija un horario valido")
                break
            print("\nEmpleado registrado con exito\n")
            print("Ingresa los datos del nuevo empleado: ")
            cliente = Empleado(nombre, apellido, DNI, dias, horarios)
            cliente.guardar_en_csv(archivo)


