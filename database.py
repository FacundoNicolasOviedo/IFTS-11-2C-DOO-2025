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
         keys = line.strip().split(",")  
         tranform = Transformador(keys)
         line = file.readline()
         while line != "":
             line = line.strip()  
             values = line.split(",")
             d = tranform.Csv2Dic(values)
             if d is not None:  
                 vectorDatabase.append(d)
             line = file.readline()
         file.close()
         return vectorDatabase
    