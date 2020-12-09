import os.path
import random

class Oportunidades:
    oportunidades = 10;
    def getOportunidades(self):
        return self.oportunidades
    def quitarOportunidad(self):
        self.oportunidades = self.oportunidades - 1
        
class Ordenamiento:
    def quickSort(self, numeros, izq, der):
        pivote = numeros[0][izq]
        aux3 = numeros[1][izq]
        i = izq
        j = der
        aux = 0
        aux2 = 0
        while i < j:
            while numeros[0][i] <= pivote and i < j:
                i += 1
            while numeros[0][j] > pivote:
                j -= 1
            if i < j:
                aux = numeros[0][i]
                aux2 = numeros[1][i]
                numeros[0][i] = numeros[0][j]
                numeros[1][i] = numeros[1][j]
                numeros[0][j] = aux
                numeros[1][j] = aux2
        numeros[0][izq] = numeros[0][j]
        numeros[1][izq] = numeros[1][j]
        numeros[0][j] = pivote
        numeros[1][j] = aux3
        if izq < j-1:
            self.quickSort(numeros,izq,j-1)
        if j+1 < der:
            self.quickSort(numeros,j+1,der)
    def ordenAlfabetico(self, nuevaPalabra):
        palabras = []
        with open("palabras.txt", "r+") as archivo:
            cadena = archivo.read()
            cantidad = cadena.count(",") + 1
        palabras = cadena.split(",")
        palabras[palabras.__len__() - 1] = nuevaPalabra
        numeros = []
        for i in range(cantidad):
            numeros.append(i)
        letras = []
        for i in range(cantidad):
            letras.append(str(ord(palabras[i][0].upper()))+str(ord(palabras[i][1].upper()))+str(ord(palabras[i][2].upper()))+str(ord(palabras[i][3].upper())))
        for i in range(cantidad):
            letras[i] = int(letras[i])
        palabras2 = [letras, numeros]
        self.quickSort(palabras2, 0, cantidad-1)
        palabrasEnOrden = []
        for i in range(cantidad):
            palabrasEnOrden.append(palabras[palabras2[1][i]])
        cadenafinal = ""
        for i in range(cantidad):
            cadenafinal = cadenafinal + palabrasEnOrden[i] + ","
        with open("palabras.txt", "r+") as archivo:
             archivo.write(cadenafinal.upper())
            
class Archivo:
    def validarPalabrasIngresadas(self, palabra):
        palabra = palabra.upper()
        while len(palabra) < 4 and palabra != "2":
            palabra = input("\nLa palabra debe contener al menos 4 caracteres, ingrese una nueva:\n")
        if palabra != "2":
            bandera = True
        else:
            bandera = False
        while(bandera):
            for i in range(len(palabra)):
                if i >= len(palabra):
                    continue
                if ord(palabra[i]) < 65 or ord(palabra[i]) > 91:
                    palabra = input("\nLa palabra debe contener unicamente letras, ingrese una nueva:\n")
                    while len(palabra) < 4 and palabra != "2":
                        palabra = input("\nLa palabra debe contener al menos 4 caracteres, ingrese una nueva:\n")
                    palabra = palabra.upper()
                    i = 0
            bandera = False
        return palabra        
    def crearArchivo(self):
        archivo = open("palabras.txt", "w")
        archivo.close()
        print("\nEl archivo se creo exitosamente")
    def verificarArchivo(self):
        if not os.path.isfile("palabras.txt"):
            print("\nEl archivo no exise")
            self.crearArchivo()
        else:
            with open("palabras.txt", "r+") as archivo:
                cadena = archivo.read()
                palabras = cadena.count(",")
            if palabras > 0:
                print("\nArchivo leido exitosamente\nEl archivo contiene "+str(palabras)+" palabras.")
            else:
                print("\nArchivo leido exitosamente\nEl archivo no contiene palabras...")
    def agregarPalabras(self):
        if not os.path.isfile("palabras.txt"):
            print("\nNo existe un archivo donde insertar las palabras.\nCreando archivo...")
            self.crearArchivo()
        print("\n--- Agregar palabras | Instrucciones ---\n\n1.- Escriba la palabra que desee y oprima enter para agregarla\n2.- Cada palabra debe contener un minimo de 4 letras\n3.- Cuando haya terminado de agregar palabras, ingrese un \'2\'")
        palabra = ""
        while palabra!="2":
            palabra = input()
            palabra = self.validarPalabrasIngresadas(palabra)
            if(palabra=="2"):
                break
            orden = Ordenamiento()
            orden.ordenAlfabetico(palabra)
        print("Las palabras se han agregado con exito")
    def eliminarArchivo(self):
        if os.path.isfile("palabras.txt"):
            os.remove("palabras.txt")
            print("\nEl archivo se elimino con exito")
        else:
            print("\nNo se ha encontrado un archivo para eliminar")
            
class JuegoAhorcado:
    def cargarPalabras(self):
        with open("palabras.txt", "r+") as archivo:
            cadena = archivo.read()
        palabras = cadena.split(",")
        palabras.pop(len(palabras)-1)
        print("\nSe han cargado "+str(len(palabras))+" palabras con exito")
        return palabras
    def elegirPalabra(self, palabras):
        azar = random.randint(0, len(palabras)-1)
        return palabras[azar]
