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
    
def registrarNuevoCliente():
    nombre = input("Ingrese su nombre")
    apellido = input("Ingrese su apellido")
    DNI = input("ingrese su DNI")

def menu():    
     print("Bienvenido a la peluqueria El Viejo Manos de Peine")
     print("Seleccione una opción")
     print("1. Registrar nuevo cliente")
     print("2. Solicitar turno") 
     print("3. Listar turnos existentes") 
     print("4. Modificar o cancelar turno") 
     print("5. Guardar datos en CSV / Cargar desde dict") 
     print("6. Salir") 
     n = input("Seleccione una opción: ")
     if n == "3":
         print("holaaa")
         

menu()

db = Database("Clientes.csv")
registros = db.read()
print(registros)


