import sys
import time
from tkinter import filedialog

gramaticas = list()

class gramatica:
    def __init__(self, Nombre, Terminales, NoTerminales, Inicial, Producciones):
        self.nombre = Nombre
        self.terminales = Terminales
        self.NoTerminales = NoTerminales
        self.inicial = Inicial
        self.producciones = Producciones

def glc(lista):
    contador = 0
    for x in range(len(lista)):
        if lista[x] == '*':
            Nombre = lista[x-contador]
            contador -= 1
            varios = lista[x-contador].split(';')
            contador -= 1
            NoTerminales = varios[0].split(',')
            Terminales = varios[1].split(',')
            Inicial = varios[2]
            Producciones = list()
            while contador != 0:
                Producciones.append(lista[x-contador])
                contador -= 1
            gramaticas.append(gramatica(Nombre,Terminales,NoTerminales,Inicial,Producciones))                        
        else:
            contador += 1

def menu():
    print('[LFP]Proyecto2')
    print('Desarrollador:')
    print('     Joaquin Emmanuel Aldair Coromac Huezo')
    print('     ---201903873---')
    for i in reversed(range(0, 6)):
        time.sleep(1)
        print("%s\r" %i)
    print('¡Bienvenido!')

    while True:
        print('-----------------Menu Principal------------------')
        print('1.Cargar Archivo')
        print('2.Mostrar información general de la gramática')
        print('3.Generar autómata de pila equivalente')
        print('4.Reporte de recorrido')
        print('5.Reporte en tabla')
        print('6.Salir')
        opcion = input('> Ingrese una opcion\n')
        if opcion == '1':
            print('----------Cargar Archivo----------')
            entrada = filedialog.askopenfilename(title='Cargar Archivo', filetypes=(('glc files','*.glc'),('all files','*.')))
            archivo = list()
            f = open(entrada, 'r')
            lineas = f.readlines()
            for x in range(len(lineas)):
                lineas[x] = lineas[x].rstrip('\n')
                if lineas[x].strip():
                    archivo.append(lineas[x])
            glc(archivo)
            f.close()
            print('------- Se ha Cargado los archivos correctamente-------')
        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
        elif opcion == '4':
            pass
        elif opcion == '5':
            pass
        elif opcion == '6':
            sys.exit()
        else:
            print('No ha seleccionado una opcion correcta')
