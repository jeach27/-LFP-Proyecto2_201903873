import sys
import time
from tkinter import filedialog
import os
import webbrowser

gramaticas = list()
automatasP = list()

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
            aviso = None
            while contador != 0:
                pro = lista[x-contador].split('->')
                expre = pro[1].split(' ')
                if len(expre) == 3:
                    if expre[2] in Terminales:
                        aviso = True
                Producciones.append(pro)
                contador -= 1
            if aviso == True:
                if len(gramaticas) == 0:
                    gramaticas.append(gramatica(Nombre,Terminales,NoTerminales,Inicial,Producciones))
                else:
                    for i in range(len(gramaticas)):
                        if gramaticas[i].nombre != Nombre:
                            gramaticas.append(gramatica(Nombre,Terminales,NoTerminales,Inicial,Producciones))
                        else:
                            print('> La Gramatica '+ Nombre +' ya existe\n')
                           
            else:
                print('> La Gramatica '+ Nombre +' no es exclusiva libre de contexto\n')                     
        else:
            contador += 1

def grafica(gram):
    file = open(gram.nombre+'.dot','w')
    file.write('digraph G{\n')
    file.write('rankdir=LR\n')
    terminales = None
    for i in range(len(gram.terminales)):
        if i == 0:
            terminales = gram.terminales[i]
        else:
            terminales = terminales + ', '+ gram.terminales[i]
    Noterminales = None
    for i in range(len(gram.NoTerminales)):
        if i == 0:
            Noterminales = gram.NoTerminales[i]
        else:
            Noterminales = Noterminales + ', '+ gram.NoTerminales[i]

    file.write('A[label="Nombre: AP_'+gram.nombre+'",shape="underline"]\n')
    file.write('F[label="Terminales: {'+terminales+'}",shape="none"]\n')
    file.write('B[label="Alfabeto de Pila: {'+terminales+', '+Noterminales+', # }",shape="none"]\n')
    file.write('C[label="Estados: { i, p, q, f }",shape="none"]\n')
    file.write('D[label="Estado Inicial: { i }",shape="none"]\n')
    file.write('E[label="Estado de Aceptacion: { f }",shape="none"]\n')
    
    
    file.write('G[label="i",shape="circle"]\n')
    file.write('H[label="p",shape="circle"]\n')
    file.write('I[label="q",shape="circle"]\n')
    file.write('J[label="f",shape="doublecircle"]\n')
    file.write('G -> H [label="$, $, #"]\n')
    file.write('H -> I [label="$, $, '+gram.inicial+'"]\n')
    file.write('I -> J [label="$, #, $"]\n')
    file.write('I -> I [label="hola"]\n')
    file.write('I -> I [label="world"]\n')
    
    
    file.write('\n')


    file.write('}')
    file.close()
    os.system('dot -Tpng '+gram.nombre+'.dot -o '+gram.nombre+'.png')
    os.startfile(gram.nombre+'.png')

def HTML_grafica(gram):
    f = open('AP_Equivalente.html','w')
    f.write('<html>\n')
    f.write('   <head>\n')
    f.write(' <title>Tabla Simbolos Menu</title>\n')
    f.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">\n')
    f.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>\n')
    f.write('<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/solid.css">\n')
    f.write('<script src="https://use.fontawesome.com/releases/v5.0.7/js/all.js"></script>\n')
    f.write('   </head>\n')
    f.write('   <body>\n')
    
    f.write('<h1>hello</h1>')
    f.write('   </body>\n')
    f.write('</html>\n')
    
    f.close()

    webbrowser.open_new_tab('AP_Equivalente.html')

def menu():
    print('\n-------------[LFP]Proyecto2-------------------')
    print('\nDesarrollador:')
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
            print('----------Cargar Archivo----------\n')
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
            print('> Se ha cargado el archivo correctamente\n')

        elif opcion == '2':
            print('----------Mostrar información general de la gramática-----------\n')
            if len(gramaticas) != 0:
                print('Gramaticas Ingresadas\n')
                for i in range(len(gramaticas)):
                    print(str(i+1)+'. '+gramaticas[i].nombre)
                gr = int(input('> Ingrese una opcion\n'))
                gro = gramaticas[gr-1]
                print('\n         Nombre de la gramatica tipo 2: '+gro.nombre)
                print('         No terminales', end=': ')
                print(gro.NoTerminales)
                print('         Terminales', end=': ')
                print(gro.terminales)
                print('         No terminal Inicial', end=': ')
                print(gro.inicial)
                print('         Producciones:\n')
                for x in range(len(gro.producciones)):
                    pro = gro.producciones[x]
                    print('             '+str(pro[0]),end=' -> ')
                    derecha = pro[1].split(' ')
                    if len(derecha) > 2:
                        print(derecha[0]+' '+derecha[1])
                        contador = 2
                        while contador < len(derecha):
                            if len(derecha) > contador+1:
                                print('                | '+derecha[contador]+' '+derecha[contador+1])
                                contador += 2
                            else:
                                print('                | '+derecha[contador])
                                contador += 1
                    else:
                        if len(derecha) == 2:
                            print(derecha[0]+' '+derecha[1])
                        else:
                            print(derecha[0])

            else:
                print('> No se ha cargado ningun archivo\n')

        elif opcion == '3':
            print('---------------Generar autómata de pila equivalente-------------\n')
            if len(gramaticas) != 0:
                print('Gramaticas Ingresadas\n')
                for i in range(len(gramaticas)):
                    print(str(i+1)+'. '+gramaticas[i].nombre)
                gr = int(input('> Ingrese una opcion\n'))
                gro = gramaticas[gr-1]
                HTML_grafica(gro)   
                grafica(gro)   
            else:
                print('> No se ha cargado ningun archivo\n')

        elif opcion == '4':
            print('-------------------------Reporte de recorrido-------------------\n')

        elif opcion == '5':
            print('------------------------Reporte en tabla------------------------\n')

        elif opcion == '6':
            sys.exit()

        else:
            print('No ha seleccionado una opcion correcta\n')