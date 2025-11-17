class Transformador(object):
    def __init__(self, atributos):
        self.keys = atributos

    def Csv2Dic(self, values):
        if len(values) != len(self.keys):
            return None
        d = {}
        i = 0
        while i < len(values):
            d[self.keys[i]] = values[i]
            i = i + 1
        return d

class Database(object):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        file = open(self.filename, "rt")
        line = file.readline()
        vectorDatabase = []
        if line == "":
            return []
        keys = line.split(";")
        tranform = Transformador(keys)
        line = file.readline()
        while line != "":
            values = line.split(";")
            d = tranform.Csv2Dic(values)
            vectorDatabase.append(d)
            line = file.readline()
        file.close()
        return vectorDatabase
    
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

class Empleado(object):

    def __init__(self, nombre, apellido, DNI, dias, horarios):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.dias = dias
        self.horarios = horarios

    
    def agregar_a_csv(nombre_archivo):    
        file = open(nombre_archivo, "at")
        print("Ingresa los datos del nuevo Empleado: ")
        Empleado.nombre = input("Ingrese su nombre: ")
        while Empleado.nombre != "":
              Empleado.apellido = input("Ingrese su apellido: ")
              Empleado.DNI = input("ingrese su DNI: ")
              Empleado.dias = input("ingrese el día que trabaja: ")
              Empleado.horarios = input("Ingrese el horario que hace: ")
              vectorDatabase = [Empleado.nombre, Empleado.apellido, Empleado.DNI, Empleado.dias, Empleado.horarios]
              fila = ",".join(vectorDatabase) + "\n"
              file.writelines([fila])
              Empleado.nombre = input("Ingrese su nombre: ")
        file.close()

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
         db = Database("Clientes.csv")
         registros = db.read()
         print(registros)
         menu()
     elif n == "2":
         Cliente.agregar_a_csv("Clientes.csv")
         menu()
     elif n == "3":
         db = Database("Empleados.csv")
         registros = db.read()
         print(registros)
         menu()
     elif n == "4":
         Empleado.agregar_a_csv("Empleados.csv")
     elif n == "5":
         db = Database("Turnos.csv")
         registros = db.read()
         print(registros)
         menu()
     elif n == "9":
         print("Usted ha salido del sistema")
        
        
menu()




