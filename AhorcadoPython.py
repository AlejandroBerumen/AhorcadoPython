import os.path

class Oportunidades:
    oportunidades = 10;
    def getOportunidades(self):
        return self.oportunidades
    def quitarOportunidad(self):
        self.oportunidades = self.oportunidades - 1
class Archivo:
    def verificarArchivo(self):
        if not os.path.isfile("palabras.txt"):
            print("\nEl archivo no exise")
            archivo = open("palabras.txt", "w")
            archivo.close()
            print("El archivo se creo exitosamente")
        else:
            with open("palabras.txt", "r+") as archivo:
                cadena = archivo.read()
                palabras = cadena.count(",")
            print("\nArchivo leido exitosamente\nEl archivo contiene "+str(palabras)+" palabras.")
            
    #def agregarPalbras(self):
        
    #def eliminarArchivo(self):
        
      
archivo = Archivo()
archivo.verificarArchivo()