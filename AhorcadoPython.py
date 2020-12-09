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
            if palabras > 0:
                print("\nArchivo leido exitosamente\nEl archivo contiene "+str(palabras)+" palabras.")
            else:
                print("\nArchivo leido exitosamente\nEl archivo no contiene palabras...")
    #def agregarPalbras(self):
        
    def eliminarArchivo(self):
        if os.path.isfile("palabras.txt"):
            os.remove("palabras.txt")
            print("\nEl archivo se elimino con exito")
        else:
            print("\nNo se ha encontrado un archivo para eliminar")