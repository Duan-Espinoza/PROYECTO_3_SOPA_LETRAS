#Clase requisitos
from tkinter import *
from tkinter import messagebox
from tkinter import font
import tkinter.font as tkFont
from tkinter import ttk
from dificultadPalabras import *
from random import choice, shuffle


class FormaPalabra:
        #Constructor
        def __init__(self, largo, palabras):
                self.largo=largo
                self.palabras=palabras
                #Tablero
                self.tablero = [[None for _ in range(self.largo)] for _ in range(self.largo)]
                self.res={}
                condicion=False
                while not condicion:
                        self.crea_tablero()
                        condicion=self.llenar_con_listaPalabras()
                        
                self.llenar_con_letras()

        #MÉTODOS

        

        #Método para obtener el tablero final en un print
        #Usada para visualizar la conducta de la clase
        def obtenerTableroFina(self):
                for x in self.tablero:
                        a=str(x)+"\n"
                        print(a)

        #Método para la orientación de las palabras con respecto al tablero
        def generarOrientacion(self,largoPalabra):
                comienzoX=0
                comienzoY=comienzoX
                finX=self.largo
                finY=finX
                eleccion=choice(range(0,4))

                if eleccion==0:#Horizontal
                        ox=1
                        oy=0
                        finX=self.largo-largoPalabra
                elif eleccion==1:#Vertical hacia arriba
                        ox=0
                        oy=1
                        finY=self.largo-largoPalabra
                elif eleccion==2:#Diagonal hacia arriba
                        ox=1
                        oy=-1
                        comienzoY=largoPalabra
                        finX=self.largo-largoPalabra
                        
                elif eleccion==3:#Diagonal hacia abajo
                        ox=1
                        oy=1
                        finY=self.largo-largoPalabra
                        finX=self.largo-largoPalabra

                x=choice(range(comienzoX,finX))
                y=choice(range(comienzoY,finY))

                return x,y,ox,oy




        #Revisa si la palabra es posible de agregar
        def revisarTablero(self,palabra,x,y,ox,oy):
                for n,letra in enumerate(palabra):
                        coordenadaX=x+n*ox
                        coordenadaY=y+n*oy
                        if self.tablero[coordenadaY][coordenadaX] != letra and self.tablero[coordenadaY][coordenadaX]:
                                return False
                return True

                
        #Agrega la palabra en la sección "res" que es repuestas, esta ultima guarda palabras y posiciones de la palabra
        def agregar_palabra(self,palabra):
                x, y, ox, oy = self.generarOrientacion(len(palabra))
                contador=0
                #Valida posiciones
                while not self.revisarTablero(palabra,x,y,ox,oy):
                        x,y,ox,oy=self.generarOrientacion(len(palabra))
                        contador+=1
                        if contador>20000:
                                return False
                #Coordenadas 
                self.res[palabra]=set()
                
                for n,letra in enumerate(palabra):
                        coordenadaX=x+n*ox
                        coordenadaY=y+n*oy
                        self.tablero[coordenadaY][coordenadaX]=letra
                        self.res[palabra].add((letra,coordenadaX,coordenadaY))

                return True



        #Inicia tablero
        def crea_tablero(self):
                for i in range(self.largo):
                        for j in range(self.largo):
                                self.tablero[i][j] = None

        #Agrega las posiciones de la palabra a buscar en el tablero
        def llenar_con_Palabras(self):
                for palabra in self.palabras:
                        revision=self.agregar_palabra(palabra)
                        if not revision:
                                return False
                return True
                

                
        #Llena con letras de caracter aleatorio el tablero
        def llenar_con_letras(self):
                for i in range(self.largo):
                        for j in range(self.largo):
                                if not self.tablero[i][j]:
                                        self.tablero[i][j]=choice('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')

        #Agrega las posiciones de las palabras (que están almacenadas en una lista) a buscar en el tablero
        def llenar_con_listaPalabras(self):
                for palabra in self.palabras:
                        res=self.agregar_palabra(palabra)
                        if not res:
                                return False
                return True
                


                
