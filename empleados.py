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