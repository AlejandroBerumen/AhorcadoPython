import os.path
import random

class Oportunidades:
    oportunidades = 10;
    def getOportunidades(self):
        return self.oportunidades
    def setOportunidades(self, opors):
        self.oportunidades = opors
    def quitarOportunidad(self):
        self.oportunidades = self.oportunidades - 1

class Validacion:
    def validarLetras(self, cadena):
        pila = Pila()
        letrasIngresadas = pila.getLetras()
        cadena = cadena.upper()
        while len(cadena) > 1 or ord(cadena[0]) < 65 or ord(cadena[0]) > 91:
            cadena = input("\nPor favor, ingrese solo una letra...\n")
        for i in range(len(letrasIngresadas)):
            if letrasIngresadas[i].upper() == cadena:
                cadena = input("\nParece que esa letra ya ha sido ingresada, intentelo nuevamente:\n")
                i = 0
                while len(cadena) > 1 or ord(cadena[0]) < 65 or ord(cadena[0]) > 91:
                    cadena = input("\nPor favor, ingrese solo una letra...\n")
        return cadena
    def validarEleccionMenu(self, elec):
        if len(elec) > 1 or ord(elec[0]) < 49 or ord(elec[0]) > 53:
            elec = input("\nEntrada no valida, intentelo de nuevo...\n")
        return elec
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
            return False
        else:
            with open("palabras.txt", "r+") as archivo:
                cadena = archivo.read()
                palabras = cadena.count(",")
            if palabras > 0:
                print("\nArchivo leido exitosamente\nEl archivo contiene "+str(palabras)+" palabras.")
                return True
            else:
                print("\nArchivo leido exitosamente\nEl archivo no contiene palabras...")
                return False
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
    def seAdivinoLaPalabra(self, palabra, pila):
        letrasIngresadas = []
        letrasIngresadas = pila.getLetras()
        cont = 0
        retorno = False
        for i in range(len(palabra)):
            for j in range(len(letrasIngresadas)):
                if letrasIngresadas[j] == None:
                    break
                if palabra.lower()[i] == letrasIngresadas[j].lower()[0]:
                    cont+=1
        if len(palabra) == cont:
            retorno = True
        return retorno
    def letrasDisponibles(self, pila):
        letrasIngresadas = []
        letrasIngresadas = pila.getLetras()
        retorno = "abcdefghijklmnopqrstuvwxyz";
        for i in range(len(retorno)):
            for j in range(len(letrasIngresadas)):
                if letrasIngresadas[j] == None:
                    break
                if retorno.lower()[i] == letrasIngresadas[j].lower()[0]:
                    retorno = retorno.replace(letrasIngresadas[j].lower(), "-")
        return retorno;
    def obtenerPalabraAdivinada(self, palabra, pila):
        letrasIngresadas = []
        letrasIngresadas = pila.getLetras()
        z = ""
        for i in range(len(palabra)):
            existio = False
            for j in range(len(letrasIngresadas)):
                if letrasIngresadas[j] == None:
                    break
                if palabra.lower()[i] == letrasIngresadas[j].lower()[0]:
                    z = z + " " + letrasIngresadas[j].lower()
                    existio = True
            if not existio:
                z = z + " -"
        return z;
    def aparicionLetra(self, palabra, letra):
        retorno = False
        for i in range(len(palabra)):
            if palabra[i] == letra:
                retorno = True
        return retorno
    def inicioAhorcado(self, palabraSecreta):
        print("\n\n----- Bienvenido al juego del ahorcado -----")
        oportunidades = Oportunidades()
        pila = Pila()
        validacion = Validacion()
        oportunidades.setOportunidades(10)
        print("\nEstoy pensando en una palabra... Puedes adivinarla?")
        while not self.seAdivinoLaPalabra(palabraSecreta, pila):
            print("\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
            print("Te quedan "+str(oportunidades.getOportunidades())+" oportunidades...")
            print(self.obtenerPalabraAdivinada(palabraSecreta, pila))
            print("Letras disponibles: "+self.letrasDisponibles(pila))
            nuevaLetra = input("Ingresa una letra:\n")
            nuevaLetra = validacion.validarLetras(nuevaLetra)
            pila.agregarLetra(nuevaLetra)
            if self.aparicionLetra(palabraSecreta, nuevaLetra):
                print("\nMuy bien!")
            else:
                print("\nOh oh... Parece que esa letra no esta en la palabra")
                oportunidades.quitarOportunidad()
            if(oportunidades.getOportunidades == 0):
                print("\nSE ACABARON LAS OPORTUNIDADES, HAS PERDIDO!")
                print("La palabra secreta era: "+palabraSecreta)
                break
            if self.seAdivinoLaPalabra(palabraSecreta, pila):
                print("\nPalabra secreta: "+palabraSecreta)
                print("FELICIDADES! HAS GANADO!")
                
class Pila:
    letras = []
    def getLetras(self):
        return self.letras
    def setLetras(self, letras):
        self.letras=letras
    def extraer(self):
        if self.getLetras() == []:
            return " "
        else:
            return self.letras.pop(0)
    def agregarLetra(self, letra):
        letras2=[]
        letras2.append(letra)
        while not self.letras == []:
            letras2.append(self.letras.pop())
        aux=0
        for i in range(1,len(letras2)):
            aux = letras2[i]
            j = (i-1)
            while j >= 0 and letras2[j] > aux:
                letras2[j+1] = letras2[j]
                letras2[j] = aux
                j -= 1
        self.setLetras(letras2)

print("\n=================== Proyecto Final de Estructura de Datos - Lauro Alejandro Berumen Fernandez - 3er Semestre ===================")
elec = "0"
juego = JuegoAhorcado()
validacion = Validacion()
archivo = Archivo()
while elec != "5":
    print("\n\nBienvenido! Que deseas hacer?")
    print("1.- Verificar archivo")
    print("2.- Llenar archivo con palabras")
    print("3.- Borrar archivo")
    print("4.- Jugar")
    print("5.- Salir")
    elec = input()
    elec = validacion.validarEleccionMenu(elec)
    if(elec=="1"):
        archivo.verificarArchivo()
    if(elec=="2"):
        archivo.agregarPalabras()
    if(elec=="3"):
        archivo.eliminarArchivo()
    if(elec=="4"):
        juego.inicioAhorcado(juego.elegirPalabra(juego.cargarPalabras()))
    