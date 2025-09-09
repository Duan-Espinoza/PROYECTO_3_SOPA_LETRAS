#Proyecto 3
#Duan Antonio Espinoza Olivares
#Axel Lopez Cruz
#Sopa letras 

#Importación de librerias necesarias para el programa*
from tkinter import *
from tkinter import messagebox
from tkinter import font
import tkinter.font as tkFont
from tkinter import ttk
from gestionPalabras import*
from dificultadPalabras import*
from generarTablero import*
from validarNickname import*
from Estadistica import*
import random
from os import listdir, getcwd
from random import choice
from functools import partial
import time


#Menu principal
def menu():
        menu_principal=Tk()
        menu_principal.geometry("500x700+200+65")
        menu_principal.resizable(False,False)
        menu_principal.title("Sopa de letras")
        menu_principal.config(bg="gray")
        titulo = Label(menu_principal,text="Sopa de letras",bg="gray",fg="white",font=('Broadway 35 bold'))
        titulo.place(x=75,y=0)
        jugar=Button(menu_principal,text="Jugar",bg="green",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:tipoJuego(menu_principal))
        jugar.place(x=85,y=100)
        idioma=Button(menu_principal,text="Idioma",bg="purple",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:menuIdioma(menu_principal))
        idioma.place(x=85,y=200)
        pregunta=Button(menu_principal,text="Palabras",bg="blue",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:palabraMenu(menu_principal))
        pregunta.place(x=85,y=300)
        busqueda=Button(menu_principal,text="Ayuda",bg="orange",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:ayudaJuego(menu_principal))
        busqueda.place(x=85,y=400)
        total=Button(menu_principal,text="Estadísticas",bg="black",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:estadistica(menu_principal))
        total.place(x=85,y=500)
        salir=Button(menu_principal,text="Salir",bg="red",fg="white",width=20,font=('Helvetica 20 bold'),command=salir_menu)
        salir.place(x=85,y=600)
        menu_principal.mainloop()


#Funcion de salir
#E:.................
#S:Salir del programa
#R:.........................
def salir_menu():
        return exit()

#Funcion de retorno
#E:Menu
#S: Retorno al menú principal
#R:...........................
def volver_menu(menu_aux):
        menu_aux.destroy()
        return menu()

#Funcion de retorno
#E:Menu
#S: Retorno al menú principal
#R:...........................
def volver_menuEnglish(menu_aux):
        menu_aux.destroy()
        return menu_english()


#Menu que permite el cambio de idioma del programa
def menuIdioma(menu):
        menu.destroy()
        menuIdioma=Tk()
        menuIdioma.title("Idioma")  
        menuIdioma.geometry("600x400+300+5")
        menuIdioma.resizable(False,False)
        menuIdioma.config(bg="gray")

        
        #Label de titulo
        titulo=Label(menuIdioma,text="Seleccione el idioma del programa",bg="gray",fg="white",font=('Broadway 15 bold'))
        titulo.place(x=100,y=10)
        espannol=Button(menuIdioma,text="Español",bg="dark blue",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:ir_version_espannol(menuIdioma))
        espannol.place(x=120,y=100)
        ingles=Button(menuIdioma,text="Inglés",bg="purple",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:ir_version_english(menuIdioma))
        ingles.place(x=120,y=200)
        volver=Button(menuIdioma,text="Volver",bg="red",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:volver_menu(menuIdioma))
        volver.place(x=120,y=300)
        menuIdioma.mainloop()


#Funcion de retorno al programa en español
#E:Menu
#S: Retorno al menú principal
#R:...........................
def ir_version_espannol(menu_aux):
        menu_aux.destroy()
        return menu()

#Funcion de retorno al programa en inglés
#E:Menu
#S: Retorno al menú principal
#R:...........................
def ir_version_english(menu_aux):
        menu_aux.destroy()
        return menu_english()




#Submenú que muestra estadística
def estadistica(menu):
        menu.destroy()
        menuEstadistica=Tk()
        menuEstadistica.title("Estadísticas de jugadores")  
        menuEstadistica.geometry("600x400+300+5")
        menuEstadistica.resizable(False,False)
        menuEstadistica.config(bg="gray")

        condicion=None
        
        #Label de titulo
        titulo=Label(menuEstadistica,text="Seleccione el tipo de estadística que desea ver",bg="gray",fg="white",font=('Broadway 15 bold'))
        titulo.place(x=15,y=10)
        duracionB=Button(menuEstadistica,text="Duración",bg="dark blue",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:estadistica2(menuEstadistica,condicion=True))
        duracionB.place(x=120,y=100)
        contrarrelojB=Button(menuEstadistica,text="Contrarreloj",bg="purple",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:estadistica2(menuEstadistica,condicion=False))
        contrarrelojB.place(x=120,y=200)
        volver=Button(menuEstadistica,text="Volver",bg="red",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:volver_menu(menuEstadistica))
        volver.place(x=120,y=300)
        menuEstadistica.mainloop()

#Función auxiliar de estadística, la cual se encarga de clasificar los datos y sacar el top 3 de los jugadores
#Uso de la clase llamada "Estadística"
def estadistica2(menuEstadistica,condicion):
        if condicion:
                titulo="Clasificación de jugadores por duración"
                info=Estadistica("jugadores.txt")
                escrito=info.verTotal("duracion")
                return estadistica3(menuEstadistica,titulo,escrito)
        else:
                titulo="Clasificación de jugadores por contrarreloj"
                info=Estadistica("jugadores.txt")
                escrito=info.verTotal("contrarreloj")
                return estadistica3(menuEstadistica,titulo,escrito)

#Interfaz del programa que muestra la información solicitada
def estadistica3(menu,titulo,escrito):
        menu.destroy()
        clasificacionEstadistica=Tk()
        clasificacionEstadistica.geometry("600x600+300+5")
        clasificacionEstadistica.resizable(False,False)
        clasificacionEstadistica.title("Clasificación")
        clasificacionEstadistica.config(bg="gray")
        #Label de titulo
        titulo=Label(clasificacionEstadistica,text=titulo,bg="gray",fg="white",font=('Broadway 15 bold'))
        titulo.place(x=25,y=10)
        #Widget de textbox
        texto = Text(clasificacionEstadistica,font =('Helvetica 15 bold'), height=19, width=45)
        texto.pack(side=LEFT, fill="y")
        mensaje=escrito

        texto.insert(END, mensaje)
        texto.config(state='disabled')
        texto.place(x=40, y=55)
        #Botón de volver
        volver=Button(clasificacionEstadistica,text="Volver",bg="red",fg="white",width=25,font=('Helvetica 15 bold'),command=lambda:estadistica(clasificacionEstadistica))
        volver.place(x=135,y=545)
        clasificacionEstadistica.mainloop()

        




#Submenú de agregar llamada
def tipoJuego(menu):
        menu.destroy()
        menuTipoJuego=Tk()
        menuTipoJuego.title("Tipo de Juego")  
        menuTipoJuego.geometry("600x550+300+5")
        menuTipoJuego.resizable(False,False)
        menuTipoJuego.config(bg="gray")
        
        #Label de titulo
        titulo=Label(menuTipoJuego,text="Tipo de Juego",bg="gray",fg="white",font=('Broadway 30 bold'))
        titulo.place(x=125,y=10)
        #Label jugabilidad
        jugabilidad=Label(menuTipoJuego,text="Jugabilidad:",bg="gray",fg="white",font=("Stencil","20"),width=("12"),height=("3")).place(x=5,y=100)
        #Label dificultad
        dificultad=Label(menuTipoJuego,text="Dificultad:",bg="gray",fg="white",font=("Stencil","20"),width=("12"),height=("3")).place(x=5,y=200)
        #Label "opcion preguntas"
        tipoPalabra=Label(menuTipoJuego,text="Palabras:",bg="gray",fg="white",font=("Stencil","20"),width=("12"),height=("3")).place(x=5,y=300)
        
        #Widget spinbox jugabilidad
        jugabilidadSet=StringVar()
        jugabilidadSpinbox=Spinbox(menuTipoJuego,state= "readonly",values=("Básico","Duración","Contrarreloj"),textvariable=jugabilidadSet,font=("Stencil",25,),width=15,bg="powder blue").place(x=220,y=125)
        #Widget spinbox dificultad
        dificultadSet=StringVar()
        dificultadSpinbox=Spinbox(menuTipoJuego,state= "readonly",values=("Principiante","Intermedio","Avanzado"),textvariable=dificultadSet,font=("Stencil",25,),width=15,bg="powder blue").place(x=220,y=225)

        #Widget spinbox tipo palabras
        palabraSet=StringVar()
        palabraSpinbox=Spinbox(menuTipoJuego,state= "readonly",values=("Manual","Aleatorio"),textvariable=palabraSet,font=("Stencil",25,),width=15,bg="powder blue").place(x=220,y=325)
  
        #Botones
        Boton1=Button(menuTipoJuego,text="Aceptar",bg="#0B6121",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:compruebaInfo(menuTipoJuego,jugabilidadSet,dificultadSet,palabraSet))
        Boton1.place(x=11,y=450)
        Boton2=Button(menuTipoJuego,text="Volver",bg="#B40404",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:volver_menu(menuTipoJuego))
        Boton2.place(x=300,y=450)

        menuTipoJuego.mainloop()


#Comprueba los datos recibidos
#E: Ventana, tipo de jugabilidad, dificultad, palabra
#S: Ventana del juego
#R: ....................
def compruebaInfo(menuTipoJuego,jugabilidad,dificultad,palabra):
        jugabilidad1=jugabilidad.get()
        dificultad1=dificultad.get()
        palabra1=palabra.get()
        if palabra1=="Aleatorio":
                
                if jugabilidad1=="Básico":
                        if dificultad1=="Principiante":
                                generarpalabras=dificultadPalabras("Palabras.txt")
                                generarpalabras1=generarpalabras.Principiante()
                                return sopaLetrasBasico(menuTipoJuego,12,generarpalabras1)
                        elif dificultad1=="Intermedio":
                                generarpalabras=dificultadPalabras("Palabras.txt")
                                generarpalabras1=generarpalabras.Intermedio()
                                return sopaLetrasBasico(menuTipoJuego,20,generarpalabras1)
                        else:
                                generarpalabras=dificultadPalabras("Palabras.txt")
                                generarpalabras1=generarpalabras.Avanzado()
                                return sopaLetrasBasico(menuTipoJuego,28,generarpalabras1)
                        
                elif jugabilidad1=="Duración":
                        if dificultad1=="Principiante":
                                generarpalabras=dificultadPalabras("Palabras.txt")
                                generarpalabras1=generarpalabras.Principiante()
                                return sopaLetrasDuracion(menuTipoJuego,12,generarpalabras1)
                        elif dificultad1=="Intermedio":
                                generarpalabras=dificultadPalabras("Palabras.txt")
                                generarpalabras1=generarpalabras.Intermedio()
                                return sopaLetrasDuracion(menuTipoJuego,20,generarpalabras1)
                        else:
                                generarpalabras=dificultadPalabras("Palabras.txt")
                                generarpalabras1=generarpalabras.Avanzado()
                                return sopaLetrasDuracion(menuTipoJuego,28,generarpalabras1)
                        
                elif jugabilidad1=="Contrarreloj":
                        if dificultad1=="Principiante":
                                generarpalabras=dificultadPalabras("Palabras.txt")
                                generarpalabras1=generarpalabras.Principiante()
                                return sopaLetrasContrarreloj(menuTipoJuego,12,generarpalabras1)
                        elif dificultad1=="Intermedio":
                                generarpalabras=dificultadPalabras("Palabras.txt")
                                generarpalabras1=generarpalabras.Intermedio()
                                return sopaLetrasContrarreloj(menuTipoJuego,20,generarpalabras1)
                        else:
                                generarpalabras=dificultadPalabras("Palabras.txt")
                                generarpalabras1=generarpalabras.Avanzado()
                                return sopaLetrasContrarreloj(menuTipoJuego,28,generarpalabras1)        
                                
        else:
                return creaPalabrasManual(menuTipoJuego,jugabilidad1,dificultad1)


#Función que se encarga de la selección de palabras "manuales"
def creaPalabrasManual(menuTipoJuego,jugabilidad,dificultad):
        if dificultad=="Principiante":
                return creaPalabrasManual2(menuTipoJuego,12,6,jugabilidad)
        elif dificultad=="Intermedio":
                return creaPalabrasManual2(menuTipoJuego,20,10,jugabilidad)
        else:
                return creaPalabrasManual2(menuTipoJuego,28,14,jugabilidad)


#Función auxiliar creaPalabrasManual que muestra la interfaz para la creación de palabras manuales
def creaPalabrasManual2(menu,largoP,cantidadP,jugabilidad):
        menu.destroy()
        menucreaPalabra=Tk()
        menucreaPalabra.title("Agregar palabra")  
        menucreaPalabra.geometry("600x300+300+5")
        menucreaPalabra.resizable(False,False)
        menucreaPalabra.config(bg="gray")

        #globales
        global lista
        global contador
        lista=[]
        contador=0
        
        
        
        #Label de titulo
        titulo=Label(menucreaPalabra,text="Agregar palabras",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=185,y=10)
        #Palabra
        palabra=Label(menucreaPalabra,text="Palabra:",bg="#ffffff",fg="black",font=("Stencil","10"),width=("15"),height=("3")).place(x=10,y=80)
        palabraSet=StringVar()
        entradaPalabra=Entry(menucreaPalabra, font=("Stencil",25,'bold'),width=20,textvariable=palabraSet,bg="powder blue", justify="left").place(x=160,y=85)

        #Botones
        Boton1=Button(menucreaPalabra,text="Crear",bg="#0B6121",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:creaPalabrasManual3(menucreaPalabra,palabraSet,largoP,cantidadP,jugabilidad))
        Boton1.place(x=11,y=200)
        Boton2=Button(menucreaPalabra,text="Volver",bg="#B40404",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:tipoJuego(menucreaPalabra))
        Boton2.place(x=300,y=200)

        menucreaPalabra.mainloop()

#Función auxiliar creaPalabrasManual2 que verifica las condiciones de las palabras ingresadas y
#En caso de que cumplan las condiciones, ingresarlas al juego
#E: Ventana,palabra,dificultad (cantidad filas), cantidad de palabras y jugabilidad
#S: Juego
#R: No se deben repetir palabras, minimo de 3 carácteres y no excederse en la cantidad de filas segun la dificultad
def creaPalabrasManual3(menucreaPalabra,palabraSet,largoP,cantidadP,jugabilidad):
        global lista
        global contador
        
        if contador==cantidadP-1:
                
                palabraNueva=palabraSet.get()
                palabraNueva=palabraNueva.upper()
                
                if NoSeRepite(palabraNueva,lista) and ( 3<=len(palabraNueva) and len(palabraNueva)<=largoP):
                        if jugabilidad=="Básico":
                                lista+=[palabraNueva]
                                return sopaLetrasBasico(menucreaPalabra,largoP,lista)
                        elif jugabilidad=="Duración":
                                lista+=[palabraNueva]
                                return sopaLetrasDuracion(menucreaPalabra,largoP,lista)
                                
                        else:
                                lista+=[palabraNueva]
                                return sopaLetrasContrarreloj(menucreaPalabra,largoP,lista)
                else:
                        return messagebox.showerror(message="La palabra introducida no es válida", title="Error")
        else:
                palabraNueva=palabraSet.get()
                palabraNueva=palabraNueva.upper()
                
                if NoSeRepite(palabraNueva,lista) and ( 3<=len(palabraNueva) and len(palabraNueva)<=largoP):
                        lista+=[palabraNueva]
                        contador+=1
                        messagebox.showinfo(message="La palabra se ha agregada con éxito, quedan "+str(cantidadP-contador), title="Estado")
                        
                                
                else:
                        return messagebox.showerror(message="La palabra introducida no es válida", title="Error")



                           
#Verifica que la lista de palabras agregadas por el usuario no se repitan
#E: Palabra y lista
#S:Valor booleano
#R:...........
def NoSeRepite(palabra,lista):
        while lista!=[]:
                if lista[0]==palabra:
                        messagebox.showerror(message="La palabra introducida ya existe", title="Error")
                        return False
                else:
                        lista=lista[1:]
        return True
        
        
#Función que redirecciona al juego de tipo básico
def sopaLetrasBasico(menu,largo,palabras):
        juegoSopaLetrasBasica(menu,largo,palabras)
#Función que redirecciona al juego de tipo duración
def sopaLetrasDuracion(menu,largo,palabras):
        juegoSopaLetrasDuracion(menu,largo,palabras)
#Función que redirecciona al juego de tipo contrarreloj
#Pero antes, solicita el tipo de contrarreloj que desea jugar
def sopaLetrasContrarreloj(menu,largo,palabras):
        menu.destroy()
        menutipoTiempo=Tk()
        menutipoTiempo.title("Tipo de contrarreloj")  
        menutipoTiempo.geometry("600x400+300+5")
        menutipoTiempo.resizable(False,False)
        menutipoTiempo.config(bg="gray")

        condicion=None
        
        #Label de titulo
        titulo=Label(menutipoTiempo,text="Seleccione el tipo de contrarreloj",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=50,y=10)
        predeterminado=Button(menutipoTiempo,text="Predeterminado",bg="green",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:verCondicion(menutipoTiempo,largo,palabras,condicion=True))
        predeterminado.place(x=120,y=100)
        manual=Button(menutipoTiempo,text="Manual",bg="purple",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:verCondicion(menutipoTiempo,largo,palabras,condicion=False))
        manual.place(x=120,y=200)
        #Botón volver
        volver=Button(menutipoTiempo,text="Volver",bg="red",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:tipoJuego(menutipoTiempo))
        volver.place(x=120,y=300)
        menutipoTiempo.mainloop()


#Verifica si el usuario quiere el tiempo predeterminado asignado por la dificultad o desea personalizar su tiempo
def verCondicion(menu,largo,palabras,condicion):
        if condicion==True:
                if largo==12:
                        cantTiempo=60
                        juegoSopaLetrasContrarreloj(menu,largo,palabras,cantTiempo)
                elif largo==20:
                        cantTiempo=120
                        juegoSopaLetrasContrarreloj(menu,largo,palabras,cantTiempo)
                else:
                        cantTiempo=180
                        juegoSopaLetrasContrarreloj(menu,largo,palabras,cantTiempo)
        else:
                return sopaLetrasContrarrelojManual(menu,largo,palabras)


#Interfaz de la cantidad de tiempo deseado
def  sopaLetrasContrarrelojManual(menu,largo,palabras):
        menu.destroy()
        menucantSegundos=Tk()
        menucantSegundos.title("Cantidad de tiempo")  
        menucantSegundos.geometry("600x300+300+5")
        menucantSegundos.resizable(False,False)
        menucantSegundos.config(bg="gray")
        
        #Label de titulo
        titulo=Label(menucantSegundos,text="Tiempo en segundos",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=100,y=10)
        #Palabra
        segundosLabel=Label(menucantSegundos,text="Segundos:",bg="#ffffff",fg="black",font=("Stencil","10"),width=("15"),height=("3")).place(x=10,y=80)
        segundosSet=StringVar()
        entradaSegundos=Entry(menucantSegundos, font=("Stencil",25,'bold'),width=20,textvariable=segundosSet,bg="powder blue", justify="left").place(x=160,y=85)

        #Botones
        Boton1=Button(menucantSegundos,text="Jugar",bg="#0B6121",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:verCondicion2(segundosSet,menucantSegundos,largo,palabras))
        Boton1.place(x=11,y=200)
        Boton2=Button(menucantSegundos,text="Volver",bg="#B40404",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:tipoJuego(menucantSegundos))
        Boton2.place(x=300,y=200)

        menucantSegundos.mainloop()


#Función que verifica si la cantidad de segundos introducida es válida
#E: Numeros
#S: Juego
#R: Debe entrar números y estos deben ser mayor a 0 y menor a 10000
def verCondicion2(segundosSet,menu,largo,palabras):
        cantSegundos=segundosSet.get()
        
        if cantSegundos.isnumeric() and 0<int(cantSegundos)<10000:
                cantTiempo=int(cantSegundos)
                juegoSopaLetrasContrarreloj(menu,largo,palabras,cantTiempo)
        else:
                messagebox.showerror(message="La entrada introducida no es válida", title="Error")
                
        

                     

#Menu interfaz preguntas
def palabraMenu(menu):
        menu.destroy()
        menuPalabra=Tk()
        menuPalabra.title("Palabras")  
        menuPalabra.geometry("600x550+300+5")
        menuPalabra.resizable(False,False)
        menuPalabra.config(bg="gray")

        #Label de titulo
        titulo=Label(menuPalabra,text="Palabras",bg="gray",fg="white",font=('Broadway 30 bold'))
        titulo.place(x=200,y=10)


        #Botones
        Boton1=Button(menuPalabra,text="Crear palabras",bg="#0B6121",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:crearPalabras(menuPalabra))
        Boton1.place(x=175,y=100)
        Boton2=Button(menuPalabra,text="Modificar palabras",bg="purple",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:modificarPalabras(menuPalabra))
        Boton2.place(x=175,y=200)
        Boton3=Button(menuPalabra,text="Eliminar palabras",bg="red",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:eliminarPalabras(menuPalabra))
        Boton3.place(x=175,y=300)
        Boton4=Button(menuPalabra,text="Volver",bg="black",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:volver_menu(menuPalabra))
        Boton4.place(x=175,y=400)
        
        menuPalabra.mainloop()



##########
#Sección del banco de palabras

#Menu creación palabras
def crearPalabras(menu):
        menu.destroy()
        menucreaPalabra=Tk()
        menucreaPalabra.title("Crear palabra")  
        menucreaPalabra.geometry("600x300+300+5")
        menucreaPalabra.resizable(False,False)
        menucreaPalabra.config(bg="gray")
        
        #Label de titulo
        titulo=Label(menucreaPalabra,text="Crear palabras",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=185,y=10)
        #Palabra
        palabra=Label(menucreaPalabra,text="Palabra:",bg="#ffffff",fg="black",font=("Stencil","10"),width=("15"),height=("3")).place(x=10,y=80)
        palabraSet=StringVar()
        entradaPalabra=Entry(menucreaPalabra, font=("Stencil",25,'bold'),width=20,textvariable=palabraSet,bg="powder blue", justify="left").place(x=160,y=85)

        #Botones
        Boton1=Button(menucreaPalabra,text="Crear",bg="#0B6121",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:agregarPalabra(palabraSet))
        Boton1.place(x=11,y=200)
        Boton2=Button(menucreaPalabra,text="Volver",bg="#B40404",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:palabraMenu(menucreaPalabra))
        Boton2.place(x=300,y=200)

        menucreaPalabra.mainloop()

#Función para agregar palabras
#E:Palabra
#S: Palabra agregada en archivo txt
#R: Cumpla los requerimientos
def agregarPalabra(palabraSet):
        palabra=palabraSet.get()
        palabra=palabra.upper()
        palabraNueva=gestionPalabras("Palabras.txt")
        palabraNueva.agregarPalabra(palabra)

        

#Menu modificar palabras
def modificarPalabras(menu):
        menu.destroy()
        menumodificarPalabra=Tk()
        menumodificarPalabra.title("Modificar palabra")  
        menumodificarPalabra.geometry("600x400+300+5")
        menumodificarPalabra.resizable(False,False)
        menumodificarPalabra.config(bg="gray")
        
        #Label de titulo
        titulo=Label(menumodificarPalabra,text="Modificar palabras",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=185,y=10)
        #Palabra a modificar
        palabramod=Label(menumodificarPalabra,text="Palabra a modificar:",bg="#ffffff",fg="black",font=("Stencil","10"),width=("18"),height=("3")).place(x=10,y=80)
        palabramodSet=StringVar()
        entradaPalabramod=Entry(menumodificarPalabra, font=("Stencil",25,'bold'),width=20,textvariable=palabramodSet,bg="powder blue", justify="left").place(x=185,y=85)
        #Palabra nueva
        palabraNueva=Label(menumodificarPalabra,text="Palabra nueva:",bg="#ffffff",fg="black",font=("Stencil","10"),width=("18"),height=("3")).place(x=10,y=200)
        palabraNuevaSet=StringVar()
        entradaPalabraNueva=Entry(menumodificarPalabra, font=("Stencil",25,'bold'),width=20,textvariable=palabraNuevaSet,bg="powder blue", justify="left").place(x=185,y=200)


        #Botones
        Boton1=Button(menumodificarPalabra,text="Modificar",bg="#0B6121",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:cambiaPalabra(palabramodSet,palabraNuevaSet))
        Boton1.place(x=11,y=300)
        Boton2=Button(menumodificarPalabra,text="Volver",bg="#B40404",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:palabraMenu(menumodificarPalabra))
        Boton2.place(x=300,y=300)

        menumodificarPalabra.mainloop()


#Función para modificar palabras
def cambiaPalabra(palabra1,palabra2):
        palabraset1=palabra1.get()
        palabraset1=palabraset1.upper()
        palabraset2=palabra2.get()
        palabraset2=palabraset2.upper()
        palabraCambio=gestionPalabras("Palabras.txt")
        palabraCambio.modificarPalabra(palabraset1,palabraset2)


#Menu eliminación palabras
def eliminarPalabras(menu):
        menu.destroy()
        menuborraPalabra=Tk()
        menuborraPalabra.title("Eliminar palabra")  
        menuborraPalabra.geometry("600x300+300+5")
        menuborraPalabra.resizable(False,False)
        menuborraPalabra.config(bg="gray")
        
        #Label de titulo
        titulo=Label(menuborraPalabra,text="Eliminar palabras",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=185,y=10)
        #Palabra
        palabra=Label(menuborraPalabra,text="Palabra:",bg="#ffffff",fg="black",font=("Stencil","10"),width=("15"),height=("3")).place(x=10,y=80)
        palabraSet=StringVar()
        entradaCodigo=Entry(menuborraPalabra, font=("Stencil",25,'bold'),width=20,textvariable=palabraSet,bg="powder blue", justify="left").place(x=160,y=85)

        #Botones
        Boton1=Button(menuborraPalabra,text="Eliminar",bg="#0B6121",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:borraPalabra(palabraSet))
        Boton1.place(x=11,y=200)
        Boton2=Button(menuborraPalabra,text="Volver",bg="#B40404",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:palabraMenu(menuborraPalabra))
        Boton2.place(x=300,y=200)

        menuborraPalabra.mainloop()


#Función para borrar palabras
def borraPalabra(palabraSet):
        palabra=palabraSet.get()
        palabra=palabra.upper()
        palabraNueva=gestionPalabras("Palabras.txt")
        palabraNueva.eliminarPalabra(palabra)


################
#################
#Clase juego básico
#Sopa letras básica
class juegoSopaLetrasBasica:
        def __init__(self,menu,largo,palabras):
                #Constructor
                menu.destroy()
                menuBasico = Tk()
                menuBasico.title('Sopa letras básica')
                menuBasico.resizable(False, False)

                
                #Frame que contendrá la sopa de letras
                self.cuadrilla_letras = Frame(menuBasico)
                #Frame que contendrá las palabras a encontrar
                self.cuadro_palabras = Frame(menuBasico)
                #Frame que contendrá los botones volver y mostrar solución
                self.menu = Frame(menuBasico)

                self.verRespuesta = False
                self.largo = largo
                self.color = "brown"

                #Cóndiciones de botones al ser presionados
                self.presionado=set()
                self.palabras=palabras
                #Cuadrilla de botones en limpio
                self.botones=[]
                for f in range(self.largo):
                        fila=[]
                        for c in range(self.largo):
                                fila.append(Button(self.cuadrilla_letras,padx=5, command=partial(self.click_evento, f, c)
                                ))
                                fila[-1].grid(row=f, column=c, sticky='ew')
                        self.botones.append(fila)

                #Labels y botones solución y volver
                titulo=Label(self.menu, text='Menu', pady=5, font=('bold')).grid(row=0, column=0, columnspan=2, sticky='ew')
                # Botón de solución
                self.solucionB=Button(self.menu, text='Solución', padx=1, pady=1, command=self.solucionarTodo).grid(row=1, column=0, sticky='ew')
                #Botón de volver al juego
                self.volver = Button(self.menu, text='Volver', padx=1, pady=1, command=lambda:self.volverJuego(menuBasico)).grid(row=1, column=1, sticky='ew')

                self.labels = {}
                self.busqueda_palabra = None
                self.crear_labels()
                self.hacer_tablero()

                #Posiciones de los frames

                self.cuadrilla_letras.pack(side=LEFT)
                self.menu.pack(side=TOP, pady=self.largo)
                self.cuadro_palabras.pack(side=TOP, padx=40, pady=20)

                menuBasico.mainloop()



        #Métodos

        #Método volver
        def volverJuego(self,menuBasico):
                return tipoJuego(menuBasico)


        #Método muestra como labels las palabras a jugar
        def crear_labels(self):
                for label in self.labels.values():
                        label.destroy()
                self.labels.clear()
                self.labels = {'Palabras': Label(self.cuadro_palabras, text='Palabras', pady=5, font=('bold'))}
                self.labels['Palabras'].grid(row=2, column=0, columnspan=2)
                for pos, palabra in enumerate(sorted(self.palabras)):
                        self.labels[palabra] = Label(self.cuadro_palabras, text=palabra, anchor='w')
                        self.labels[palabra].grid(row=(pos // 2) + (pos % 1) + 3, column=pos % 2, sticky='W')


        #Método que registra los eventos de los botones de la sopa de letras 
        def click_evento(self, fila, columna):
                contador=0
                if self.botones[fila][columna].cget('bg') == self.color:
                        self.botones[fila][columna].configure(bg='SystemButtonFace')
                        self.presionado.remove((self.botones[fila][columna].cget('text'), columna, fila))
                else:
                        self.botones[fila][columna].configure(bg=self.color)
                        self.presionado.add((self.botones[fila][columna].cget('text'), columna, fila))
                        for palabra, coordenadas in self.clase_genera_tablero.res.items():
                                #El uso "&" verifica las condiciones como un "and" pero bit por bit
                                if coordenadas & self.presionado == coordenadas:
                                        contador+=1
                                        if contador==len(self.palabras):
                                                messagebox.showinfo(message="Felicidades: Has solucionado todas las palabras", title="Estado")
                                        else:
                                                for _, c, f in coordenadas:
                                                        self.botones[f][c].configure(state=DISABLED)
                                                self.labels[palabra].configure(bg=self.color)


        #Método que muestra la solución total de la sopa de letras
        def solucionarTodo(self):
                if self.verRespuesta:
                        bg = 'SystemButtonFace'
                        state = NORMAL
                        self.presionado.clear()
                else:
                        bg = self.color
                        state = DISABLED
                        messagebox.showwarning(message="Fin del juego", title="Estado")
                        

                self.verRespuesta = not self.verRespuesta
                for palabra, coordenadas in self.clase_genera_tablero.res.items():
                        self.labels[palabra].configure(bg=bg)
                        for _, c, f in coordenadas:
                                self.botones[f][c].configure(state=state, bg=bg)

        #Función que hace llamada a la clase "FormaPalabra" para formar la cuadrilla a usar del tablero
        #esta a su vez cambia los botones a lo que está en la matriz formada por "FormaPalabra"
        def hacer_tablero(self):

                if self.verRespuesta:
                        self.verRespuesta = not self._solution_shown
                self.clase_genera_tablero = FormaPalabra(self.largo, self.palabras)
                self.presionado.clear()

                for f in range(self.largo):
                        for c in range(self.largo):
                                self.botones[f][c].configure(text=self.clase_genera_tablero.tablero[f][c], bg='SystemButtonFace',state=NORMAL)

                for label in self.labels.values():
                        label.configure(bg='SystemButtonFace')




###########
#############
#Clase juego duración
class juegoSopaLetrasDuracion:
        def __init__(self,menu,largo,palabras):
                #Constructor
                menu.destroy()
                global menuDuracion
                menuDuracion = Tk()
                menuDuracion.title('Sopa letras duración')
                menuDuracion.resizable(False, False)
                
                #Frame que contendrá la sopa de letras
                self.cuadrilla_letras = Frame(menuDuracion)
                #Frame que contendrá las palabras a encontrar
                self.cuadro_palabras = Frame(menuDuracion)
                #Frame que contendrá los botones volver y mostrar solución
                self.menu = Frame(menuDuracion)
                #Frame que contendrá el cronómetro
                self.cuadroTiempo=Frame(menuDuracion)

                self.verRespuesta = False
                self.largo = largo
                self.color = "brown"

                #Cóndiciones de botones al ser presionados
                self.presionado=set()
                self.palabras=palabras
                #Cuadrilla de botones en limpio
                self.botones=[]
                for f in range(self.largo):
                        fila=[]
                        for c in range(self.largo):
                                fila.append(Button(self.cuadrilla_letras,padx=5, command=partial(self.click_evento, f, c)
                                ))
                                fila[-1].grid(row=f, column=c, sticky='ew')
                        self.botones.append(fila)

                #Labels y botones solución y volver
                titulo=Label(self.menu, text='Menu', pady=5, font=('bold')).grid(row=0, column=0, columnspan=2, sticky='ew')
                # Botón de solución
                self.solucionB=Button(self.menu, text='Solución', padx=1, pady=1, command=self.solucionarTodo)
                self.solucionB.grid(row=1, column=0, sticky='ew')
                #Botón de volver al juego
                self.volver = Button(self.menu, text='Volver', padx=1, pady=1, command=lambda:self.volverJuego(menuDuracion)).grid(row=1, column=1, sticky='ew')
                #Label y cronómetro
                tituloTiempo=Label(self.cuadroTiempo, text='Tiempo:', pady=5, font=('bold')).grid(row=0, column=0, columnspan=2, sticky='ew')
                #cronómetro
                
                self.segundos=0
                self.crono=Label(self.cuadroTiempo,text="", pady=8, font=('bold'))
                self.crono.grid(row=2, column=0, columnspan=2, sticky='ew')

                self.labels = {}
                self.busqueda_palabra = None
                self.crear_labels()
                self.hacer_tablero()

                #Posiciones de los frames

                self.cuadrilla_letras.pack(side=LEFT)
                self.menu.pack(side=TOP, pady=self.largo)
                self.cuadro_palabras.pack(side=TOP, padx=40, pady=20)
                self.cuadroTiempo.pack(side=TOP, pady=self.largo)
                #Inicia el tiempo
                self.tiempo()
                

                menuDuracion.mainloop()



        #Métodos
        #Método que inicia un cronómetro (en segundos)
        def tiempo(self):
                self.segundos=self.segundos+1
                self.crono.configure(text=str(self.segundos)+ " segundos")
                self.detener=self.cuadroTiempo.after(1000, self.tiempo)

        #Método que para el tiempo
        def parartiempo(self):
                self.cuadroTiempo.after_cancel(self.detener)
                self.crono.configure(text=str(self.segundos)+ " segundos")

        #Método volver
        def volverJuego(self,menuBasico):
                self.parartiempo()
                return tipoJuego(menuBasico)


        #Método que muestra como labels las palabras a jugar
        def crear_labels(self):
                for label in self.labels.values():
                        label.destroy()
                self.labels.clear()
                self.labels = {'Palabras': Label(self.cuadro_palabras, text='Palabras', pady=5, font=('bold'))}
                self.labels['Palabras'].grid(row=2, column=0, columnspan=2)
                for pos, palabra in enumerate(sorted(self.palabras)):
                        self.labels[palabra] = Label(self.cuadro_palabras, text=palabra, anchor='w')
                        self.labels[palabra].grid(row=(pos // 2) + (pos % 1) + 3, column=pos % 2, sticky='W')


        #Método que registra los eventos de los botones de la sopa de letras
        def click_evento(self, fila, columna):
                contador=0
                if self.botones[fila][columna].cget('bg') == self.color:
                        self.botones[fila][columna].configure(bg='SystemButtonFace')
                        self.presionado.remove((self.botones[fila][columna].cget('text'), columna, fila))
                else:
                        self.botones[fila][columna].configure(bg=self.color)
                        self.presionado.add((self.botones[fila][columna].cget('text'), columna, fila))
                        for palabra, coordenadas in self.clase_genera_tablero.res.items():
                                #El uso "&" verifica las condiciones como un "and" pero bit por bit
                                if coordenadas & self.presionado == coordenadas:
                                        contador+=1
                                        if contador==len(self.palabras):
                                                self.parartiempo()
                                                messagebox.showinfo(message="Felicidades: Has solucionado todas las palabras", title="Estado")
                                                return menuVictoria(menuDuracion,"duracion",self.segundos,self.largo)
                                        else:
                                                for _, c, f in coordenadas:
                                                        self.botones[f][c].configure(state=DISABLED)
                                                self.labels[palabra].configure(bg=self.color)


        #Método que muestra la solución total de la sopa de letras
        def solucionarTodo(self):
                bg = self.color
                state = DISABLED
                self.parartiempo()
                messagebox.showwarning(message="Fin del juego", title="Estado")
                self.solucionB.configure(state=state)
                          

                self.verRespuesta = not self.verRespuesta
                for palabra, coordenadas in self.clase_genera_tablero.res.items():
                        self.labels[palabra].configure(bg=bg)
                        for _, c, f in coordenadas:
                                self.botones[f][c].configure(state=state, bg=bg)

        #Función que hace llamada a la clase "FormaPalabra" para formar la cuadrilla a usar del tablero
        #esta a su vez cambia los botones a lo que está en la matriz formada por "FormaPalabra"
        def hacer_tablero(self):

                if self.verRespuesta:
                        self.verRespuesta = not self._solution_shown
                self.clase_genera_tablero = FormaPalabra(self.largo, self.palabras)
                self.presionado.clear()

                for f in range(self.largo):
                        for c in range(self.largo):
                                self.botones[f][c].configure(text=self.clase_genera_tablero.tablero[f][c], bg='SystemButtonFace',state=NORMAL)

                for label in self.labels.values():
                        label.configure(bg='SystemButtonFace')


###########
#############
#Clase juego contrarreloj
class juegoSopaLetrasContrarreloj:
        def __init__(self,menu,largo,palabras,segundos):
                #Constructor
                menu.destroy()
                global menuContra
                menuContra = Tk()
                menuContra.title('Sopa letras contrarreloj')
                menuContra.resizable(False, False)
                
                #Frame que contendrá la sopa de letras
                self.cuadrilla_letras = Frame(menuContra)
                #Frame que contendrá las palabras a encontrar
                self.cuadro_palabras = Frame(menuContra)
                #Frame que contendrá los botones volver y mostrar solución
                self.menu = Frame(menuContra)
                #Frame que contendrá el cronómetro
                self.cuadroTiempo=Frame(menuContra)

                self.verRespuesta = False
                self.largo = largo
                self.color = "brown"

                #Cóndiciones de botones al ser presionados
                self.presionado=set()
                self.palabras=palabras
                #Cuadrilla de botones en limpio
                self.botones=[]
                for f in range(self.largo):
                        fila=[]
                        for c in range(self.largo):
                                fila.append(Button(self.cuadrilla_letras,padx=5, command=partial(self.click_evento, f, c)
                                ))
                                fila[-1].grid(row=f, column=c, sticky='ew')
                        self.botones.append(fila)

                #Labels y botones solución y volver
                titulo=Label(self.menu, text='Menu', pady=5, font=('bold')).grid(row=0, column=0, columnspan=2, sticky='ew')
                # Botón de solución
                self.solucionB=Button(self.menu, text='Solución', padx=1, pady=1, command=self.solucionarTodo)
                self.solucionB.grid(row=1, column=0, sticky='ew')
                #Botón de volver al juego
                self.volver = Button(self.menu, text='Volver', padx=1, pady=1, command=lambda:self.volverJuego(menuContra)).grid(row=1, column=1, sticky='ew')
                #Label y cronómetro
                tituloTiempo=Label(self.cuadroTiempo, text='Tiempo:', pady=5, font=('bold')).grid(row=0, column=0, columnspan=2, sticky='ew')
                #cronómetro
                
                self.segundos=segundos
                self.crono=Label(self.cuadroTiempo,text="", pady=8, font=('bold'))
                self.crono.grid(row=2, column=0, columnspan=2, sticky='ew')

                self.labels = {}
                self.busqueda_palabra = None
                self.crear_labels()
                self.hacer_tablero()

                #Posiciones de los frames

                self.cuadrilla_letras.pack(side=LEFT)
                self.menu.pack(side=TOP, pady=self.largo)
                self.cuadro_palabras.pack(side=TOP, padx=40, pady=20)
                self.cuadroTiempo.pack(side=TOP, pady=self.largo)
                #Inicia el tiempo
                self.tiempo()
                

                menuContra.mainloop()



        #Métodos
        #Método que registra el tiempo restante que le queda al usuario
        def tiempo(self):
                if self.segundos==0:
                        self.solucionarTodo()
                else:
                        self.segundos=self.segundos-1
                        self.crono.configure(text=str(self.segundos)+ " segundos")
                        self.detener=self.cuadroTiempo.after(1000, self.tiempo)

        #Método que detiene el cronómetro
        def parartiempo(self):
                self.cuadroTiempo.after_cancel(self.detener)
                self.crono.configure(text=str(self.segundos)+ " segundos")

        #Método volver
        def volverJuego(self,menuBasico):
                self.parartiempo()
                return tipoJuego(menuBasico)


        #Método que muestra como labels las palabras a jugar
        def crear_labels(self):
                for label in self.labels.values():
                        label.destroy()
                self.labels.clear()
                self.labels = {'Palabras': Label(self.cuadro_palabras, text='Palabras', pady=5, font=('bold'))}
                self.labels['Palabras'].grid(row=2, column=0, columnspan=2)
                for pos, palabra in enumerate(sorted(self.palabras)):
                        self.labels[palabra] = Label(self.cuadro_palabras, text=palabra, anchor='w')
                        self.labels[palabra].grid(row=(pos // 2) + (pos % 1) + 3, column=pos % 2, sticky='W')


        #Método que registra los eventos de los botones de la sopa de letras
        def click_evento(self, fila, columna):
                contador=0
                if self.botones[fila][columna].cget('bg') == self.color:
                        self.botones[fila][columna].configure(bg='SystemButtonFace')
                        self.presionado.remove((self.botones[fila][columna].cget('text'), columna, fila))
                else:
                        self.botones[fila][columna].configure(bg=self.color)
                        self.presionado.add((self.botones[fila][columna].cget('text'), columna, fila))
                        for palabra, coordenadas in self.clase_genera_tablero.res.items():
                                #El uso "&" verifica las condiciones como un "and" pero bit por bit
                                if coordenadas & self.presionado == coordenadas:
                                        contador+=1
                                        if contador==len(self.palabras):
                                                self.parartiempo()
                                                messagebox.showinfo(message="Felicidades: Has solucionado todas las palabras", title="Estado")
                                                return menuVictoria(menuContra,"contrarreloj",self.segundos,self.largo)
                                        else:
                                                for _, c, f in coordenadas:
                                                        self.botones[f][c].configure(state=DISABLED)
                                                self.labels[palabra].configure(bg=self.color)


        #Método que muestra la solución total de la sopa de letras
        def solucionarTodo(self):
                bg = self.color
                state = DISABLED
                self.parartiempo()
                messagebox.showwarning(message="Fin del juego", title="Estado")
                self.solucionB.configure(state=state)
                          

                self.verRespuesta = not self.verRespuesta
                for palabra, coordenadas in self.clase_genera_tablero.res.items():
                        self.labels[palabra].configure(bg=bg)
                        for _, c, f in coordenadas:
                                self.botones[f][c].configure(state=state, bg=bg)

        #Función que hace llamada a la clase "FormaPalabra" para formar la cuadrilla a usar del tablero
        #esta a su vez cambia los botones a lo que está en la matriz formada por "FormaPalabra"
        def hacer_tablero(self):

                if self.verRespuesta:
                        self.verRespuesta = not self._solution_shown
                self.clase_genera_tablero = FormaPalabra(self.largo, self.palabras)
                self.presionado.clear()

                for f in range(self.largo):
                        for c in range(self.largo):
                                self.botones[f][c].configure(text=self.clase_genera_tablero.tablero[f][c], bg='SystemButtonFace',state=NORMAL)

                for label in self.labels.values():
                        label.configure(bg='SystemButtonFace')



 #Interfaz que crea nickname y lo guarda en "jugadores.txt"               
def menuVictoria(menu,tipoJuego,tiempo,dificultad):
        menu.destroy()
        menuInfoGanador=Tk()
        menuInfoGanador.title("Información del ganador")  
        menuInfoGanador.geometry("600x300+300+5")
        menuInfoGanador.resizable(False,False)
        menuInfoGanador.config(bg="gray")
        
        #Label de titulo
        titulo=Label(menuInfoGanador,text="Introduzca su nickname",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=100,y=10)
        #Palabra
        palabra=Label(menuInfoGanador,text="nickname:",bg="#ffffff",fg="black",font=("Stencil","10"),width=("15"),height=("3")).place(x=10,y=80)
        palabraSet=StringVar()
        entradaPalabra=Entry(menuInfoGanador, font=("Stencil",25,'bold'),width=20,textvariable=palabraSet,bg="powder blue", justify="left").place(x=160,y=85)

        #Botones
        Boton1=Button(menuInfoGanador,text="Crear",bg="#0B6121",fg="white",font=("Stencil","15"),width=("35"),height=("3"),command=lambda:agregarJugador(menuInfoGanador,palabraSet,tipoJuego,tiempo,dificultad))
        Boton1.place(x=65,y=200)

        menuInfoGanador.mainloop()


#Escritura archivos en jugadores.txt
#E:Ventana, palabra,strings y numeros(indicaría el tiempo y dificultad)
#S:Escritura de archivos en jugadores.txt
#R:No deben repetirse nicknames en el modo duración con la misma dificultad
def agregarJugador(menuInfoGanador,palabraSet,estiloJuego,tiempo,dificultad):
        nickname=palabraSet.get()
        nickname=nickname.upper()
        if nickname=="" or nickname==" ":
                messagebox.showerror(message="nickname no válido", title="Error")
        else:
                if estiloJuego=="duracion":
                        if dificultad==12:
                                if seRepiteUsuario(nickname,"principiante"):
                                        messagebox.showerror(message="nickname no válido", title="Error")
                                else:
                                        file=open("jugadores.txt","a")
                                        file.write(nickname+","+estiloJuego+","+"principiante,"+str(tiempo)+"\n")
                                        file.close()
                                        return tipoJuego(menuInfoGanador)
                        elif dificultad==20:
                                if seRepiteUsuario(nickname,"intermedio"):
                                        messagebox.showerror(message="nickname no válido", title="Error")
                                else:
                                        file=open("jugadores.txt","a")
                                        file.write(nickname+","+estiloJuego+","+"intermedio,"+str(tiempo)+"\n")
                                        file.close()
                                        return tipoJuego(menuInfoGanador)
                        elif dificultad==28:
                                if seRepiteUsuario(nickname,"avanzado"):
                                        messagebox.showerror(message="nickname no válido", title="Error")
                                else:
                                        file=open("jugadores.txt","a")
                                        file.write(nickname+","+estiloJuego+","+"avanzado,"+str(tiempo)+"\n")
                                        file.close()
                                        return tipoJuego(menuInfoGanador)

                else:
                        if dificultad==12:
                                file=open("jugadores.txt","a")
                                file.write(nickname+","+estiloJuego+","+"principiante\n")
                                file.close()
                                return tipoJuego(menuInfoGanador)
                        elif dificultad==20:
                                file=open("jugadores.txt","a")
                                file.write(nickname+","+estiloJuego+","+"intermedio\n")
                                file.close()
                                return tipoJuego(menuInfoGanador)
                        elif dificultad==28:
                                file=open("jugadores.txt","a")
                                file.write(nickname+","+estiloJuego+","+"avanzado\n")
                                file.close()
                                return tipoJuego(menuInfoGanador)




#Verifica que no se repitan usuarios en modalidad de juego "Duración"
#Estos se pueden repetir solo si están en jugabilidades distintas o dificultades diferentes
#Uso de clase validarNickname
def seRepiteUsuario(nickname,dificultad):
        verifica=validarNickname("jugadores.txt")
        condicion=verifica.nicknameRepetido(nickname,dificultad)
        if condicion:
                return True
        else:
                return False


                        
                        

#Interfaz de ayuda de juego
def ayudaJuego(menu):
        menu.destroy()
        menu_ayuda=Tk()
        menu_ayuda.geometry("500x600+200+65")
        menu_ayuda.resizable(False,False)
        menu_ayuda.title("Sopa de letras")
        menu_ayuda.config(bg="gray")
        titulo = Label(menu_ayuda,text="Información del juego",bg="gray",fg="white",font=('Broadway 25 bold'))
        titulo.place(x=50,y=0)
        Menus=Button(menu_ayuda,text="Menu principal",bg="green",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:ayudaMenuP(menu_ayuda))
        Menus.place(x=85,y=100)
        juegoBasico=Button(menu_ayuda,text="Juego Básico",bg="purple",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:ayudaMenuB(menu_ayuda))
        juegoBasico.place(x=85,y=200)
        juegoDuracion=Button(menu_ayuda,text="Juego Duración",bg="blue",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:ayudaMenuD(menu_ayuda))
        juegoDuracion.place(x=85,y=300)
        juegoContra=Button(menu_ayuda,text="Juego Contrarreloj",bg="orange",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:ayudaMenuC(menu_ayuda))
        juegoContra.place(x=85,y=400)
        volver=Button(menu_ayuda,text="Volver",bg="red",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:volver_menu(menu_ayuda))
        volver.place(x=85,y=500)
        menu_ayuda.mainloop()


#Interfaz e información sobre el uso de "menú principal"
def ayudaMenuP(menu):
        menu.destroy()
        ayudaMenuPrincipal=Tk()
        ayudaMenuPrincipal.geometry("600x600+300+5")
        ayudaMenuPrincipal.resizable(False,False)
        ayudaMenuPrincipal.title("Información del programa")
        ayudaMenuPrincipal.config(bg="gray")
        #Label de titulo
        titulo=Label(ayudaMenuPrincipal,text="Información del menú principal",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=50,y=10)
        #Widget de textbox
        scroll = Scrollbar(ayudaMenuPrincipal)
        texto = Text(ayudaMenuPrincipal,font =('Helvetica 15 bold'), height=19, width=45)
        scroll.config(command=texto.yview)
        scroll.pack(side=RIGHT, fill="y")
        texto.pack(side=LEFT, fill="y")
        mensaje="""***Menu Principal***
********************
En este menu se desplegarán las opciones
(seleccionables con el mouse)
de Jugar,Idioma,Palabras,
Ayuda, Estadísticas y Salir

1-Jugar: Desplegará un menú con los
modos de juego y la dificultad deseada
-------------
2-Idioma: Permite el cambio
de idioma del programa,se desplegarán
las opciones español e inglés
-------------
3-Palabras: El banco de palabras, este permite
agregar, modificar y eliminar las palabras
que se usarán en el juego
-------------
4-Ayuda: Esta es la sección que tiene las
instrucciones de uso del programa
-------------
5-Estadísticas: Esta sección clasificará
los datos almacenados
en el archivo de texto llamado "jugadores"
este clasificará por
la jugabilidad, luego la dificultad elegida
por el jugador y al final
clasificará por mejor tiempo
en la jugabilidad "duración"
y cantidad de victorias en
la jugabilidad "contrarreloj"
--------------------------------
6-Salir: Esta sección permite cerrar el programa"""

        texto.insert(END, mensaje)
        texto.config(yscrollcommand=scroll.set)
        texto.config(state='disabled')
        texto.place(x=40, y=55)
        #Boton volver
        volver=Button(ayudaMenuPrincipal,text="Volver",bg="red",fg="white",width=25,font=('Helvetica 15 bold'),command=lambda:ayudaJuego(ayudaMenuPrincipal))
        volver.place(x=135,y=545)
        ayudaMenuPrincipal.mainloop()

#Interfaz e información sobre el uso de la jugabilidad básica de la sopa de letras
def ayudaMenuB(menu):
        menu.destroy()
        ayudaMenuJuegoBasico=Tk()
        ayudaMenuJuegoBasico.geometry("600x600+300+5")
        ayudaMenuJuegoBasico.resizable(False,False)
        ayudaMenuJuegoBasico.title("Información del juego básico")
        ayudaMenuJuegoBasico.config(bg="gray")
        #Label de titulo
        titulo=Label(ayudaMenuJuegoBasico,text="Información de la jugabilidad básica",bg="gray",fg="white",font=('Broadway 17 bold'))
        titulo.place(x=25,y=10)
        #Widget de textbox
        scroll = Scrollbar(ayudaMenuJuegoBasico)
        texto = Text(ayudaMenuJuegoBasico,font =('Helvetica 15 bold'), height=19, width=45)
        scroll.config(command=texto.yview)
        scroll.pack(side=RIGHT, fill="y")
        texto.pack(side=LEFT, fill="y")
        mensaje="""***Jugabilidad básico***
************************
En este menu se desplegarán el juego con
la jugabilidad básica, esta no posee tiempo
ni guarda datos cuando se gana
la partida. Antes de jugar
el jugador puede jugar con las
palabras del banco de palabras 
o que el jugador las introduzca
de manera manual
En el juego se desplegará
a la izquierda el tablero mientras que
la derecha cuenta con las
siguientes secciones:

----------------
1-Mostrar solución: Resuelve automáticamente
las palabras a buscar en la sopa
de letras e indica al usuario un mensaje
llamado "Fin de la partida"

-------------
2-Volver: Permite regresar a la sección
de "tipo de juego"
que permite empezar otra partida
-------------
3-Palabras: Lista de palabras que se verán
en el juego, estas se marcarán cuando sean
encontradas por el jugador, en el momento
que las encuentre todas
le saldrá un mensaje
indicándole que ha ganado la partida"""

        texto.insert(END, mensaje)
        texto.config(yscrollcommand=scroll.set)
        texto.config(state='disabled')
        texto.place(x=40, y=55)
        #Botón volver
        volver=Button(ayudaMenuJuegoBasico,text="Volver",bg="red",fg="white",width=25,font=('Helvetica 15 bold'),command=lambda:ayudaJuego(ayudaMenuJuegoBasico))
        volver.place(x=135,y=545)
        ayudaMenuJuegoBasico.mainloop()

#Interfaz e información sobre el uso de la jugabilidad "duración" de la sopa de letras
def ayudaMenuD(menu):
        menu.destroy()
        ayudaMenuJuegoDuracion=Tk()
        ayudaMenuJuegoDuracion.geometry("600x600+300+5")
        ayudaMenuJuegoDuracion.resizable(False,False)
        ayudaMenuJuegoDuracion.title("Información del juego duración")
        ayudaMenuJuegoDuracion.config(bg="gray")
        #Label de titulo
        titulo=Label(ayudaMenuJuegoDuracion,text="Información de jugabilidad duración",bg="gray",fg="white",font=('Broadway 17 bold'))
        titulo.place(x=25,y=10)
        #Widget de textbox
        scroll = Scrollbar(ayudaMenuJuegoDuracion)
        texto = Text(ayudaMenuJuegoDuracion,font =('Helvetica 15 bold'), height=19, width=45)
        scroll.config(command=texto.yview)
        scroll.pack(side=RIGHT, fill="y")
        texto.pack(side=LEFT, fill="y")
        mensaje="""***Jugabilidad duración***
************************
En este menu se desplegarán el juego 
con la jugabilidad duración, 
esta contará el tiempo que dura
el jugador en encontrar todas las palabras
en la sopa de letras, antes de jugar
el jugador puede jugar con las
palabras del banco de palabras 
o que el jugador las introduzca
de manera manual
En el juego se desplegará
a la izquierda el tablero mientras que
la derecha cuenta con las
siguientes secciones:
------------------

1-Mostrar solución: Resuelve
automáticamente las palabras a buscar
en la sopa de letras 
e indica al usuario un mensaje
llamado "Fin de la partida" y
que detiene el tiempo, al presionarlo
solo se puede volver, ya que equivale 
a rendirse

-------------
2-Volver: Permite regresar a la
sección de "tipo de juego"
que permite empezar otra partida
-------------

3-Palabras: Lista de palabras que se verán 
en el juego
estas se marcarán cuando sean encontradas 
por el jugador, en el momento que las 
encuentre todas le saldrá un mensaje 
indicándole que ha ganado la partida
y lo llevará a un menu que le permitirá
introducir su nickname y ser
registrado en la lista de 
jugadores para ver en estadística
-----------------------

4-Cronómetro: Muestra la cantidad
de tiempo restante"""

        texto.insert(END, mensaje)
        texto.config(yscrollcommand=scroll.set)
        texto.config(state='disabled')
        texto.place(x=40, y=55)
        #Botón volver
        volver=Button(ayudaMenuJuegoDuracion,text="Volver",bg="red",fg="white",width=25,font=('Helvetica 15 bold'),command=lambda:ayudaJuego(ayudaMenuJuegoDuracion))
        volver.place(x=135,y=545)
        ayudaMenuJuegoDuracion.mainloop()

#Interfaz e información sobre el uso de la jugabilidad "contrarreloj" de la sopa de letras
def ayudaMenuC(menu):
        menu.destroy()
        ayudaMenuJuegoContrarreloj=Tk()
        ayudaMenuJuegoContrarreloj.geometry("600x600+300+5")
        ayudaMenuJuegoContrarreloj.resizable(False,False)
        ayudaMenuJuegoContrarreloj.title("Información del juego contrarreloj")
        ayudaMenuJuegoContrarreloj.config(bg="gray")
        #Label de titulo
        titulo=Label(ayudaMenuJuegoContrarreloj,text="Información de jugabilidad contrarreloj",bg="gray",fg="white",font=('Broadway 17 bold'))
        titulo.place(x=15,y=10)
        #Widget de textbox
        scroll = Scrollbar(ayudaMenuJuegoContrarreloj)
        texto = Text(ayudaMenuJuegoContrarreloj,font =('Helvetica 15 bold'), height=19, width=45)
        scroll.config(command=texto.yview)
        scroll.pack(side=RIGHT, fill="y")
        texto.pack(side=LEFT, fill="y")
        mensaje="""***Jugabilidad contrarreloj***
************************
En este menu se desplegarán el juego 
con la jugabilidad contrarreloj, 
esta contará el tiempo que irá 
reduciendose hasta llegar a 0.
En el momento que se llegue a
0, mostrará todas las palabras
que se debían encontrar y
tirará el mensaje de
"Fin de la partida", en ese
momento el usuario solo podrá volver
a los tipos de juegos con el botón.
El jugador debe encontrar 
todas las palabras antes que
se le acabe el tiempo en la 
sopa de letras, antes de jugar
el jugador puede jugar con las
palabras del banco de palabras 
o que el jugador las introduzca
de manera manual al igual que 
la duración que desea del 
cronómetro, la cual puede ser
manual o predeterminada por la 
dificultad

1-Mostrar solución: Resuelve automáticamente 
las palabras a buscar en la sopa de letras 
e indica al usuario un mensaje
llamado "Fin de la partida" y
que detiene el tiempo, al presionarlo
solo se puede volver, ya que equivale 
a rendirse
-------------

2-Volver: Permite regresar a la sección de 
"tipo de juego"que permite empezar
otra partida diferente 
------------------

3-Palabras: Lista de palabras que se verán 
en el juego
estas se marcarán cuando sean encontradas 
por el jugador, en el momento que las 
encuentre todas le saldrá un mensaje 
indicándole que ha ganado la partida
y lo llevará a un menu que le permitirá
introducir su nickname y ser
registrado en la lista de 
jugadores para ver en estadística
--------------------------

4-Cronómetro: Muestra la cantidad
de tiempo restante"""

        texto.insert(END, mensaje)
        texto.config(yscrollcommand=scroll.set)
        texto.config(state='disabled')
        texto.place(x=40, y=55)
        #Botón volver
        volver=Button(ayudaMenuJuegoContrarreloj,text="Volver",bg="red",fg="white",width=25,font=('Helvetica 15 bold'),command=lambda:ayudaJuego(ayudaMenuJuegoContrarreloj))
        volver.place(x=135,y=545)
        ayudaMenuJuegoContrarreloj.mainloop()




############################
############################
############################
############################
############################
############################
############################
############################
############################
############################
############################
############################
############################
############################
############################
############################
############################






#Menu principal
def menu_english():
        menu_principal=Tk()
        menu_principal.geometry("500x700+200+65")
        menu_principal.resizable(False,False)
        menu_principal.title("Wordsearch")
        menu_principal.config(bg="gray")
        titulo = Label(menu_principal,text="Wordsearch",bg="gray",fg="white",font=('Broadway 35 bold'))
        titulo.place(x=75,y=0)
        jugar=Button(menu_principal,text="Play",bg="green",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:tipoJuegoEnglish(menu_principal))
        jugar.place(x=85,y=100)
        idioma=Button(menu_principal,text="Language",bg="purple",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:menuIdiomaEnglish(menu_principal))
        idioma.place(x=85,y=200)
        pregunta=Button(menu_principal,text="Words",bg="blue",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:palabraMenuEnglish(menu_principal))
        pregunta.place(x=85,y=300)
        busqueda=Button(menu_principal,text="Help",bg="orange",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:ayudaJuegoEnglish(menu_principal))
        busqueda.place(x=85,y=400)
        total=Button(menu_principal,text="Statistics",bg="black",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:estadisticaEnglish(menu_principal))
        total.place(x=85,y=500)
        salir=Button(menu_principal,text="Exit",bg="red",fg="white",width=20,font=('Helvetica 20 bold'),command=salir_menu)
        salir.place(x=85,y=600)
        menu_principal.mainloop()



#Menu que permite el cambio de idioma del programa
def menuIdiomaEnglish(menu):
        menu.destroy()
        menuIdioma=Tk()
        menuIdioma.title("Language")  
        menuIdioma.geometry("600x400+300+5")
        menuIdioma.resizable(False,False)
        menuIdioma.config(bg="gray")

        
        #Label de titulo
        titulo=Label(menuIdioma,text="Select the language of the game",bg="gray",fg="white",font=('Broadway 15 bold'))
        titulo.place(x=100,y=10)
        espannol=Button(menuIdioma,text="Spanish",bg="dark blue",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:ir_version_espannol(menuIdioma))
        espannol.place(x=120,y=100)
        ingles=Button(menuIdioma,text="English",bg="purple",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:ir_version_english(menuIdioma))
        ingles.place(x=120,y=200)
        volver=Button(menuIdioma,text="Return",bg="red",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:volver_menuEnglish(menuIdioma))
        volver.place(x=120,y=300)
        menuIdioma.mainloop()





#Submenú que muestra estadística
def estadisticaEnglish(menu):
        menu.destroy()
        menuEstadistica=Tk()
        menuEstadistica.title("Statistics of the player")  
        menuEstadistica.geometry("600x400+300+5")
        menuEstadistica.resizable(False,False)
        menuEstadistica.config(bg="gray")

        condicion=None
        
        #Label de titulo
        titulo=Label(menuEstadistica,text="Select the type of stadistic",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=100,y=10)
        duracionB=Button(menuEstadistica,text="Duration",bg="dark blue",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:estadisticaEnglish2(menuEstadistica,condicion=True))
        duracionB.place(x=120,y=100)
        contrarrelojB=Button(menuEstadistica,text="Time trial",bg="purple",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:estadisticaEnglish2(menuEstadistica,condicion=False))
        contrarrelojB.place(x=120,y=200)
        volver=Button(menuEstadistica,text="Return",bg="red",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:volver_menuEnglish(menuEstadistica))
        volver.place(x=120,y=300)
        menuEstadistica.mainloop()

#Función auxiliar de estadística, la cual se encarga de clasificar los datos y sacar el top 3 de los jugadores
#Uso de la clase llamada "Estadística"
def estadisticaEnglish2(menuEstadistica,condicion):
        if condicion:
                titulo="Player ranking by duration"
                info=Estadistica2("players.txt")
                escrito=info.verTotal("duracion")
                return estadisticaEnglish3(menuEstadistica,titulo,escrito)
        else:
                titulo="Player ranking by time trial"
                info=Estadistica2("players.txt")
                escrito=info.verTotal("contrarreloj")
                return estadisticaEnglish3(menuEstadistica,titulo,escrito)

#Interfaz del programa que muestra la información solicitada
def estadisticaEnglish3(menu,titulo,escrito):
        menu.destroy()
        clasificacionEstadistica=Tk()
        clasificacionEstadistica.geometry("600x600+300+5")
        clasificacionEstadistica.resizable(False,False)
        clasificacionEstadistica.title("Ranking")
        clasificacionEstadistica.config(bg="gray")
        #Label de titulo
        titulo=Label(clasificacionEstadistica,text=titulo,bg="gray",fg="white",font=('Broadway 15 bold'))
        titulo.place(x=25,y=10)
        #Widget de textbox
        texto = Text(clasificacionEstadistica,font =('Helvetica 15 bold'), height=19, width=45)
        texto.pack(side=LEFT, fill="y")
        mensaje=escrito

        texto.insert(END, mensaje)
        texto.config(state='disabled')
        texto.place(x=40, y=55)
        #Botón de volver
        volver=Button(clasificacionEstadistica,text="Return",bg="red",fg="white",width=25,font=('Helvetica 15 bold'),command=lambda:estadisticaEnglish(clasificacionEstadistica))
        volver.place(x=135,y=545)
        clasificacionEstadistica.mainloop()

        




#Submenú de agregar llamada
def tipoJuegoEnglish(menu):
        menu.destroy()
        menuTipoJuego=Tk()
        menuTipoJuego.title("Type of game")  
        menuTipoJuego.geometry("600x550+300+5")
        menuTipoJuego.resizable(False,False)
        menuTipoJuego.config(bg="gray")
        
        #Label de titulo
        titulo=Label(menuTipoJuego,text="Type of game",bg="gray",fg="white",font=('Broadway 30 bold'))
        titulo.place(x=125,y=10)
        #Label jugabilidad
        jugabilidad=Label(menuTipoJuego,text="Gameplay:",bg="gray",fg="white",font=("Stencil","20"),width=("12"),height=("3")).place(x=5,y=100)
        #Label dificultad
        dificultad=Label(menuTipoJuego,text="Difficulty:",bg="gray",fg="white",font=("Stencil","20"),width=("12"),height=("3")).place(x=5,y=200)
        #Label "opcion preguntas"
        tipoPalabra=Label(menuTipoJuego,text="Words:",bg="gray",fg="white",font=("Stencil","20"),width=("12"),height=("3")).place(x=5,y=300)
        
        #Widget spinbox jugabilidad
        jugabilidadSet=StringVar()
        jugabilidadSpinbox=Spinbox(menuTipoJuego,state= "readonly",values=("Basic","Duration","Timetrial"),textvariable=jugabilidadSet,font=("Stencil",25,),width=15,bg="powder blue").place(x=220,y=125)
        #Widget spinbox dificultad
        dificultadSet=StringVar()
        dificultadSpinbox=Spinbox(menuTipoJuego,state= "readonly",values=("Easy","Medium","Hard"),textvariable=dificultadSet,font=("Stencil",25,),width=15,bg="powder blue").place(x=220,y=225)

        #Widget spinbox tipo palabras
        palabraSet=StringVar()
        palabraSpinbox=Spinbox(menuTipoJuego,state= "readonly",values=("Manual","Random"),textvariable=palabraSet,font=("Stencil",25,),width=15,bg="powder blue").place(x=220,y=325)
  
        #Botones
        Boton1=Button(menuTipoJuego,text="Accept",bg="#0B6121",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:compruebaInfoEnglish(menuTipoJuego,jugabilidadSet,dificultadSet,palabraSet))
        Boton1.place(x=11,y=450)
        Boton2=Button(menuTipoJuego,text="Return",bg="#B40404",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:volver_menuEnglish(menuTipoJuego))
        Boton2.place(x=300,y=450)

        menuTipoJuego.mainloop()


#Comprueba los datos recibidos
#E: Ventana, tipo de jugabilidad, dificultad, palabra
#S: Ventana del juego
#R: ....................
def compruebaInfoEnglish(menuTipoJuego,jugabilidad,dificultad,palabra):
        jugabilidad1=jugabilidad.get()
        dificultad1=dificultad.get()
        palabra1=palabra.get()
        if palabra1=="Random":
                
                if jugabilidad1=="Basic":
                        if dificultad1=="Easy":
                                generarpalabras=dificultadPalabras2("Palabras2.txt")
                                generarpalabras1=generarpalabras.Principiante()
                                return sopaLetrasBasicoEnglish(menuTipoJuego,12,generarpalabras1)
                        elif dificultad1=="Medium":
                                generarpalabras=dificultadPalabras2("Palabras2.txt")
                                generarpalabras1=generarpalabras.Intermedio()
                                return sopaLetrasBasicoEnglish(menuTipoJuego,20,generarpalabras1)
                        else:
                                generarpalabras=dificultadPalabras2("Palabras2.txt")
                                generarpalabras1=generarpalabras.Avanzado()
                                return sopaLetrasBasicoEnglish(menuTipoJuego,28,generarpalabras1)
                        
                elif jugabilidad1=="Duration":
                        if dificultad1=="Easy":
                                generarpalabras=dificultadPalabras2("Palabras2.txt")
                                generarpalabras1=generarpalabras.Principiante()
                                return sopaLetrasDuracionEnglish(menuTipoJuego,12,generarpalabras1)
                        elif dificultad1=="Medium":
                                generarpalabras=dificultadPalabras2("Palabras2.txt")
                                generarpalabras1=generarpalabras.Intermedio()
                                return sopaLetrasDuracionEnglish(menuTipoJuego,20,generarpalabras1)
                        else:
                                generarpalabras=dificultadPalabras2("Palabras2.txt")
                                generarpalabras1=generarpalabras.Avanzado()
                                return sopaLetrasDuracionEnglish(menuTipoJuego,28,generarpalabras1)
                        
                elif jugabilidad1=="Timetrial":
                        if dificultad1=="Easy":
                                generarpalabras=dificultadPalabras2("Palabras2.txt")
                                generarpalabras1=generarpalabras.Principiante()
                                return sopaLetrasContrarrelojEnglish(menuTipoJuego,12,generarpalabras1)
                        elif dificultad1=="Medium":
                                generarpalabras=dificultadPalabras2("Palabras2.txt")
                                generarpalabras1=generarpalabras.Intermedio()
                                return sopaLetrasContrarrelojEnglish(menuTipoJuego,20,generarpalabras1)
                        else:
                                generarpalabras=dificultadPalabras2("Palabras2.txt")
                                generarpalabras1=generarpalabras.Avanzado()
                                return sopaLetrasContrarrelojEnglish(menuTipoJuego,28,generarpalabras1)        
                                
        else:
                return creaPalabrasManualEnglish(menuTipoJuego,jugabilidad1,dificultad1)


#Función que se encarga de la selección de palabras "manuales"
def creaPalabrasManualEnglish(menuTipoJuego,jugabilidad,dificultad):
        if dificultad=="Easy":
                return creaPalabrasManual2English(menuTipoJuego,12,6,jugabilidad)
        elif dificultad=="Medium":
                return creaPalabrasManual2English(menuTipoJuego,20,10,jugabilidad)
        else:
                return creaPalabrasManual2English(menuTipoJuego,28,14,jugabilidad)


#Función auxiliar creaPalabrasManual que muestra la interfaz para la creación de palabras manuales
def creaPalabrasManual2English(menu,largoP,cantidadP,jugabilidad):
        menu.destroy()
        menucreaPalabra=Tk()
        menucreaPalabra.title("Add words")  
        menucreaPalabra.geometry("600x300+300+5")
        menucreaPalabra.resizable(False,False)
        menucreaPalabra.config(bg="gray")

        #globales
        global lista
        global contador
        lista=[]
        contador=0
        
        
        
        #Label de titulo
        titulo=Label(menucreaPalabra,text="Add words",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=185,y=10)
        #Palabra
        palabra=Label(menucreaPalabra,text="Word:",bg="#ffffff",fg="black",font=("Stencil","10"),width=("15"),height=("3")).place(x=10,y=80)
        palabraSet=StringVar()
        entradaPalabra=Entry(menucreaPalabra, font=("Stencil",25,'bold'),width=20,textvariable=palabraSet,bg="powder blue", justify="left").place(x=160,y=85)

        #Botones
        Boton1=Button(menucreaPalabra,text="Create",bg="#0B6121",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:creaPalabrasManual3English(menucreaPalabra,palabraSet,largoP,cantidadP,jugabilidad))
        Boton1.place(x=11,y=200)
        Boton2=Button(menucreaPalabra,text="Return",bg="#B40404",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:tipoJuegoEnglish(menucreaPalabra))
        Boton2.place(x=300,y=200)

        menucreaPalabra.mainloop()

#Función auxiliar creaPalabrasManual2 que verifica las condiciones de las palabras ingresadas y
#En caso de que cumplan las condiciones, ingresarlas al juego
#E: Ventana,palabra,dificultad (cantidad filas), cantidad de palabras y jugabilidad
#S: Juego
#R: No se deben repetir palabras, minimo de 3 carácteres y no excederse en la cantidad de filas segun la dificultad
def creaPalabrasManual3English(menucreaPalabra,palabraSet,largoP,cantidadP,jugabilidad):
        global lista
        global contador
        
        if contador==cantidadP-1:
                
                palabraNueva=palabraSet.get()
                palabraNueva=palabraNueva.upper()
                
                if NoSeRepiteEnglish(palabraNueva,lista) and ( 3<=len(palabraNueva) and len(palabraNueva)<=largoP):
                        if jugabilidad=="Basic":
                                lista+=[palabraNueva]
                                return sopaLetrasBasicoEnglish(menucreaPalabra,largoP,lista)
                        elif jugabilidad=="Duration":
                                lista+=[palabraNueva]
                                return sopaLetrasDuracionEnglish(menucreaPalabra,largoP,lista)
                                
                        else:
                                lista+=[palabraNueva]
                                return sopaLetrasContrarrelojEnglish(menucreaPalabra,largoP,lista)
                else:
                        return messagebox.showerror(message="The word entered is not valid", title="Error")
        else:
                palabraNueva=palabraSet.get()
                palabraNueva=palabraNueva.upper()
                
                if NoSeRepiteEnglish(palabraNueva,lista) and ( 3<=len(palabraNueva) and len(palabraNueva)<=largoP):
                        lista+=[palabraNueva]
                        contador+=1
                        messagebox.showinfo(message="The word has been added successfully, they remain "+str(cantidadP-contador), title="Estado")
                        
                                
                else:
                        return messagebox.showerror(message="The word entered is not valid", title="Error")



                           
#Verifica que la lista de palabras agregadas por el usuario no se repitan
#E: Palabra y lista
#S:Valor booleano
#R:...........
def NoSeRepiteEnglish(palabra,lista):
        while lista!=[]:
                if lista[0]==palabra:
                        messagebox.showerror(message="The word entered already exist", title="Error")
                        return False
                else:
                        lista=lista[1:]
        return True
        
        
#Función que redirecciona al juego de tipo básico
def sopaLetrasBasicoEnglish(menu,largo,palabras):
        juegoSopaLetrasBasicaEnglish(menu,largo,palabras)
#Función que redirecciona al juego de tipo duración
def sopaLetrasDuracionEnglish(menu,largo,palabras):
        juegoSopaLetrasDuracionEnglish(menu,largo,palabras)
#Función que redirecciona al juego de tipo contrarreloj
#Pero antes, solicita el tipo de contrarreloj que desea jugar
def sopaLetrasContrarrelojEnglish(menu,largo,palabras):
        menu.destroy()
        menutipoTiempo=Tk()
        menutipoTiempo.title("Type of timetrial")  
        menutipoTiempo.geometry("600x400+300+5")
        menutipoTiempo.resizable(False,False)
        menutipoTiempo.config(bg="gray")

        condicion=None
        
        #Label de titulo
        titulo=Label(menutipoTiempo,text="Select the type of timetrial",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=50,y=10)
        predeterminado=Button(menutipoTiempo,text="Predetermined",bg="green",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:verCondicionEnglish(menutipoTiempo,largo,palabras,condicion=True))
        predeterminado.place(x=120,y=100)
        manual=Button(menutipoTiempo,text="Manual",bg="purple",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:verCondicionEnglish(menutipoTiempo,largo,palabras,condicion=False))
        manual.place(x=120,y=200)
        #Botón volver
        volver=Button(menutipoTiempo,text="Return",bg="red",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:tipoJuegoEnglish(menutipoTiempo))
        volver.place(x=120,y=300)
        menutipoTiempo.mainloop()


#Verifica si el usuario quiere el tiempo predeterminado asignado por la dificultad o desea personalizar su tiempo
def verCondicionEnglish(menu,largo,palabras,condicion):
        if condicion==True:
                if largo==12:
                        cantTiempo=60
                        juegoSopaLetrasContrarrelojEnglish(menu,largo,palabras,cantTiempo)
                elif largo==20:
                        cantTiempo=120
                        juegoSopaLetrasContrarrelojEnglish(menu,largo,palabras,cantTiempo)
                else:
                        cantTiempo=180
                        juegoSopaLetrasContrarrelojEnglish(menu,largo,palabras,cantTiempo)
        else:
                return sopaLetrasContrarrelojManualEnglish(menu,largo,palabras)


#Interfaz de la cantidad de tiempo deseado
def  sopaLetrasContrarrelojManualEnglish(menu,largo,palabras):
        menu.destroy()
        menucantSegundos=Tk()
        menucantSegundos.title("Amount of time")  
        menucantSegundos.geometry("600x300+300+5")
        menucantSegundos.resizable(False,False)
        menucantSegundos.config(bg="gray")
        
        #Label de titulo
        titulo=Label(menucantSegundos,text="Time in seconds",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=100,y=10)
        #Palabra
        segundosLabel=Label(menucantSegundos,text="Seconds:",bg="#ffffff",fg="black",font=("Stencil","10"),width=("15"),height=("3")).place(x=10,y=80)
        segundosSet=StringVar()
        entradaSegundos=Entry(menucantSegundos, font=("Stencil",25,'bold'),width=20,textvariable=segundosSet,bg="powder blue", justify="left").place(x=160,y=85)

        #Botones
        Boton1=Button(menucantSegundos,text="Play",bg="#0B6121",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:verCondicion2English(segundosSet,menucantSegundos,largo,palabras))
        Boton1.place(x=11,y=200)
        Boton2=Button(menucantSegundos,text="Return",bg="#B40404",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:tipoJuegoEnglish(menucantSegundos))
        Boton2.place(x=300,y=200)

        menucantSegundos.mainloop()


#Función que verifica si la cantidad de segundos introducida es válida
#E: Numeros
#S: Juego
#R: Debe entrar números y estos deben ser mayor a 0 y menor a 10000
def verCondicion2English(segundosSet,menu,largo,palabras):
        cantSegundos=segundosSet.get()
        
        if cantSegundos.isnumeric() and 0<int(cantSegundos)<10000:
                cantTiempo=int(cantSegundos)
                juegoSopaLetrasContrarrelojEnglish(menu,largo,palabras,cantTiempo)
        else:
                messagebox.showerror(message="The entry is not valid", title="Error")
                
        

                     

#Menu interfaz preguntas
def palabraMenuEnglish(menu):
        menu.destroy()
        menuPalabra=Tk()
        menuPalabra.title("Words")  
        menuPalabra.geometry("600x550+300+5")
        menuPalabra.resizable(False,False)
        menuPalabra.config(bg="gray")

        #Label de titulo
        titulo=Label(menuPalabra,text="Words",bg="gray",fg="white",font=('Broadway 30 bold'))
        titulo.place(x=200,y=10)


        #Botones
        Boton1=Button(menuPalabra,text="Create words",bg="#0B6121",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:crearPalabrasEnglish(menuPalabra))
        Boton1.place(x=175,y=100)
        Boton2=Button(menuPalabra,text="Modified word",bg="purple",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:modificarPalabrasEnglish(menuPalabra))
        Boton2.place(x=175,y=200)
        Boton3=Button(menuPalabra,text="Delete words",bg="red",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:eliminarPalabrasEnglish(menuPalabra))
        Boton3.place(x=175,y=300)
        Boton4=Button(menuPalabra,text="Return",bg="black",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:volver_menuEnglish(menuPalabra))
        Boton4.place(x=175,y=400)
        
        menuPalabra.mainloop()



##########
#Sección del banco de palabras

#Menu creación palabras
def crearPalabrasEnglish(menu):
        menu.destroy()
        menucreaPalabra=Tk()
        menucreaPalabra.title("Create words")  
        menucreaPalabra.geometry("600x300+300+5")
        menucreaPalabra.resizable(False,False)
        menucreaPalabra.config(bg="gray")
        
        #Label de titulo
        titulo=Label(menucreaPalabra,text="Create words",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=185,y=10)
        #Palabra
        palabra=Label(menucreaPalabra,text="Word:",bg="#ffffff",fg="black",font=("Stencil","10"),width=("15"),height=("3")).place(x=10,y=80)
        palabraSet=StringVar()
        entradaPalabra=Entry(menucreaPalabra, font=("Stencil",25,'bold'),width=20,textvariable=palabraSet,bg="powder blue", justify="left").place(x=160,y=85)

        #Botones
        Boton1=Button(menucreaPalabra,text="Create",bg="#0B6121",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:agregarPalabraEnglish(palabraSet))
        Boton1.place(x=11,y=200)
        Boton2=Button(menucreaPalabra,text="Return",bg="#B40404",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:palabraMenuEnglish(menucreaPalabra))
        Boton2.place(x=300,y=200)

        menucreaPalabra.mainloop()

#Función para agregar palabras
#E:Palabra
#S: Palabra agregada en archivo txt
#R: Cumpla los requerimientos
def agregarPalabraEnglish(palabraSet):
        palabra=palabraSet.get()
        palabra=palabra.upper()
        palabraNueva=gestionPalabras2("Palabras2.txt")
        palabraNueva.agregarPalabra(palabra)

        

#Menu modificar palabras
def modificarPalabrasEnglish(menu):
        menu.destroy()
        menumodificarPalabra=Tk()
        menumodificarPalabra.title("Modified words")  
        menumodificarPalabra.geometry("600x400+300+5")
        menumodificarPalabra.resizable(False,False)
        menumodificarPalabra.config(bg="gray")
        
        #Label de titulo
        titulo=Label(menumodificarPalabra,text="Modified words",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=185,y=10)
        #Palabra a modificar
        palabramod=Label(menumodificarPalabra,text="Word to modified:",bg="#ffffff",fg="black",font=("Stencil","10"),width=("18"),height=("3")).place(x=10,y=80)
        palabramodSet=StringVar()
        entradaPalabramod=Entry(menumodificarPalabra, font=("Stencil",25,'bold'),width=20,textvariable=palabramodSet,bg="powder blue", justify="left").place(x=185,y=85)
        #Palabra nueva
        palabraNueva=Label(menumodificarPalabra,text="New word:",bg="#ffffff",fg="black",font=("Stencil","10"),width=("18"),height=("3")).place(x=10,y=200)
        palabraNuevaSet=StringVar()
        entradaPalabraNueva=Entry(menumodificarPalabra, font=("Stencil",25,'bold'),width=20,textvariable=palabraNuevaSet,bg="powder blue", justify="left").place(x=185,y=200)


        #Botones
        Boton1=Button(menumodificarPalabra,text="Modified",bg="#0B6121",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:cambiaPalabraEnglish(palabramodSet,palabraNuevaSet))
        Boton1.place(x=11,y=300)
        Boton2=Button(menumodificarPalabra,text="Return",bg="#B40404",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:palabraMenuEnglish(menumodificarPalabra))
        Boton2.place(x=300,y=300)

        menumodificarPalabra.mainloop()


#Función para modificar palabras
def cambiaPalabraEnglish(palabra1,palabra2):
        palabraset1=palabra1.get()
        palabraset1=palabraset1.upper()
        palabraset2=palabra2.get()
        palabraset2=palabraset2.upper()
        palabraCambio=gestionPalabras2("Palabras2.txt")
        palabraCambio.modificarPalabra(palabraset1,palabraset2)


#Menu eliminación palabras
def eliminarPalabrasEnglish(menu):
        menu.destroy()
        menuborraPalabra=Tk()
        menuborraPalabra.title("Delete words")  
        menuborraPalabra.geometry("600x300+300+5")
        menuborraPalabra.resizable(False,False)
        menuborraPalabra.config(bg="gray")
        
        #Label de titulo
        titulo=Label(menuborraPalabra,text="Delete words",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=185,y=10)
        #Palabra
        palabra=Label(menuborraPalabra,text="Word:",bg="#ffffff",fg="black",font=("Stencil","10"),width=("15"),height=("3")).place(x=10,y=80)
        palabraSet=StringVar()
        entradaCodigo=Entry(menuborraPalabra, font=("Stencil",25,'bold'),width=20,textvariable=palabraSet,bg="powder blue", justify="left").place(x=160,y=85)

        #Botones
        Boton1=Button(menuborraPalabra,text="Delete",bg="#0B6121",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:borraPalabraEnglish(palabraSet))
        Boton1.place(x=11,y=200)
        Boton2=Button(menuborraPalabra,text="Return",bg="#B40404",fg="white",font=("Stencil","12"),width=("25"),height=("3"),command=lambda:palabraMenuEnglish(menuborraPalabra))
        Boton2.place(x=300,y=200)

        menuborraPalabra.mainloop()


#Función para borrar palabras
def borraPalabraEnglish(palabraSet):
        palabra=palabraSet.get()
        palabra=palabra.upper()
        palabraNueva=gestionPalabras2("Palabras2.txt")
        palabraNueva.eliminarPalabra(palabra)


################
#################
#Clase juego básico
#Sopa letras básica
class juegoSopaLetrasBasicaEnglish:
        def __init__(self,menu,largo,palabras):
                #Constructor
                menu.destroy()
                menuBasico = Tk()
                menuBasico.title('Wordsearch basic')
                menuBasico.resizable(False, False)

                
                #Frame que contendrá la sopa de letras
                self.cuadrilla_letras = Frame(menuBasico)
                #Frame que contendrá las palabras a encontrar
                self.cuadro_palabras = Frame(menuBasico)
                #Frame que contendrá los botones volver y mostrar solución
                self.menu = Frame(menuBasico)

                self.verRespuesta = False
                self.largo = largo
                self.color = "brown"

                #Cóndiciones de botones al ser presionados
                self.presionado=set()
                self.palabras=palabras
                #Cuadrilla de botones en limpio
                self.botones=[]
                for f in range(self.largo):
                        fila=[]
                        for c in range(self.largo):
                                fila.append(Button(self.cuadrilla_letras,padx=5, command=partial(self.click_evento, f, c)
                                ))
                                fila[-1].grid(row=f, column=c, sticky='ew')
                        self.botones.append(fila)

                #Labels y botones solución y volver
                titulo=Label(self.menu, text='Menu', pady=5, font=('bold')).grid(row=0, column=0, columnspan=2, sticky='ew')
                # Botón de solución
                self.solucionB=Button(self.menu, text='Solution', padx=1, pady=1, command=self.solucionarTodo).grid(row=1, column=0, sticky='ew')
                #Botón de volver al juego
                self.volver = Button(self.menu, text='Return', padx=1, pady=1, command=lambda:self.volverJuego(menuBasico)).grid(row=1, column=1, sticky='ew')

                self.labels = {}
                self.busqueda_palabra = None
                self.crear_labels()
                self.hacer_tablero()

                #Posiciones de los frames

                self.cuadrilla_letras.pack(side=LEFT)
                self.menu.pack(side=TOP, pady=self.largo)
                self.cuadro_palabras.pack(side=TOP, padx=40, pady=20)

                menuBasico.mainloop()



        #Métodos

        #Método volver
        def volverJuego(self,menuBasico):
                return tipoJuegoEnglish(menuBasico)


        #Método muestra como labels las palabras a jugar
        def crear_labels(self):
                for label in self.labels.values():
                        label.destroy()
                self.labels.clear()
                self.labels = {'Palabras': Label(self.cuadro_palabras, text='Words', pady=5, font=('bold'))}
                self.labels['Palabras'].grid(row=2, column=0, columnspan=2)
                for pos, palabra in enumerate(sorted(self.palabras)):
                        self.labels[palabra] = Label(self.cuadro_palabras, text=palabra, anchor='w')
                        self.labels[palabra].grid(row=(pos // 2) + (pos % 1) + 3, column=pos % 2, sticky='W')


        #Método que registra los eventos de los botones de la sopa de letras 
        def click_evento(self, fila, columna):
                contador=0
                if self.botones[fila][columna].cget('bg') == self.color:
                        self.botones[fila][columna].configure(bg='SystemButtonFace')
                        self.presionado.remove((self.botones[fila][columna].cget('text'), columna, fila))
                else:
                        self.botones[fila][columna].configure(bg=self.color)
                        self.presionado.add((self.botones[fila][columna].cget('text'), columna, fila))
                        for palabra, coordenadas in self.clase_genera_tablero.res.items():
                                #El uso "&" verifica las condiciones como un "and" pero bit por bit
                                if coordenadas & self.presionado == coordenadas:
                                        contador+=1
                                        if contador==len(self.palabras):
                                                messagebox.showinfo(message="You win!", title="State")
                                        else:
                                                for _, c, f in coordenadas:
                                                        self.botones[f][c].configure(state=DISABLED)
                                                self.labels[palabra].configure(bg=self.color)


        #Método que muestra la solución total de la sopa de letras
        def solucionarTodo(self):
                if self.verRespuesta:
                        bg = 'SystemButtonFace'
                        state = NORMAL
                        self.presionado.clear()
                else:
                        bg = self.color
                        state = DISABLED
                        messagebox.showwarning(message="Game over", title="State")
                        

                self.verRespuesta = not self.verRespuesta
                for palabra, coordenadas in self.clase_genera_tablero.res.items():
                        self.labels[palabra].configure(bg=bg)
                        for _, c, f in coordenadas:
                                self.botones[f][c].configure(state=state, bg=bg)

        #Función que hace llamada a la clase "FormaPalabra" para formar la cuadrilla a usar del tablero
        #esta a su vez cambia los botones a lo que está en la matriz formada por "FormaPalabra"
        def hacer_tablero(self):

                if self.verRespuesta:
                        self.verRespuesta = not self._solution_shown
                self.clase_genera_tablero = FormaPalabra(self.largo, self.palabras)
                self.presionado.clear()

                for f in range(self.largo):
                        for c in range(self.largo):
                                self.botones[f][c].configure(text=self.clase_genera_tablero.tablero[f][c], bg='SystemButtonFace',state=NORMAL)

                for label in self.labels.values():
                        label.configure(bg='SystemButtonFace')




###########
#############
#Clase juego duración
class juegoSopaLetrasDuracionEnglish:
        def __init__(self,menu,largo,palabras):
                #Constructor
                menu.destroy()
                global menuDuracion
                menuDuracion = Tk()
                menuDuracion.title('Wordsearch duration')
                menuDuracion.resizable(False, False)
                
                #Frame que contendrá la sopa de letras
                self.cuadrilla_letras = Frame(menuDuracion)
                #Frame que contendrá las palabras a encontrar
                self.cuadro_palabras = Frame(menuDuracion)
                #Frame que contendrá los botones volver y mostrar solución
                self.menu = Frame(menuDuracion)
                #Frame que contendrá el cronómetro
                self.cuadroTiempo=Frame(menuDuracion)

                self.verRespuesta = False
                self.largo = largo
                self.color = "brown"

                #Cóndiciones de botones al ser presionados
                self.presionado=set()
                self.palabras=palabras
                #Cuadrilla de botones en limpio
                self.botones=[]
                for f in range(self.largo):
                        fila=[]
                        for c in range(self.largo):
                                fila.append(Button(self.cuadrilla_letras,padx=5, command=partial(self.click_evento, f, c)
                                ))
                                fila[-1].grid(row=f, column=c, sticky='ew')
                        self.botones.append(fila)

                #Labels y botones solución y volver
                titulo=Label(self.menu, text='Menu', pady=5, font=('bold')).grid(row=0, column=0, columnspan=2, sticky='ew')
                # Botón de solución
                self.solucionB=Button(self.menu, text='Solution', padx=1, pady=1, command=self.solucionarTodo)
                self.solucionB.grid(row=1, column=0, sticky='ew')
                #Botón de volver al juego
                self.volver = Button(self.menu, text='Return', padx=1, pady=1, command=lambda:self.volverJuego(menuDuracion)).grid(row=1, column=1, sticky='ew')
                #Label y cronómetro
                tituloTiempo=Label(self.cuadroTiempo, text='Time:', pady=5, font=('bold')).grid(row=0, column=0, columnspan=2, sticky='ew')
                #cronómetro
                
                self.segundos=0
                self.crono=Label(self.cuadroTiempo,text="", pady=8, font=('bold'))
                self.crono.grid(row=2, column=0, columnspan=2, sticky='ew')

                self.labels = {}
                self.busqueda_palabra = None
                self.crear_labels()
                self.hacer_tablero()

                #Posiciones de los frames

                self.cuadrilla_letras.pack(side=LEFT)
                self.menu.pack(side=TOP, pady=self.largo)
                self.cuadro_palabras.pack(side=TOP, padx=40, pady=20)
                self.cuadroTiempo.pack(side=TOP, pady=self.largo)
                #Inicia el tiempo
                self.tiempo()
                

                menuDuracion.mainloop()



        #Métodos
        #Método que inicia un cronómetro (en segundos)
        def tiempo(self):
                self.segundos=self.segundos+1
                self.crono.configure(text=str(self.segundos)+ " seconds")
                self.detener=self.cuadroTiempo.after(1000, self.tiempo)

        #Método que para el tiempo
        def parartiempo(self):
                self.cuadroTiempo.after_cancel(self.detener)
                self.crono.configure(text=str(self.segundos)+ " seconds")

        #Método volver
        def volverJuego(self,menuBasico):
                self.parartiempo()
                return tipoJuegoEnglish(menuBasico)


        #Método que muestra como labels las palabras a jugar
        def crear_labels(self):
                for label in self.labels.values():
                        label.destroy()
                self.labels.clear()
                self.labels = {'Palabras': Label(self.cuadro_palabras, text='Words', pady=5, font=('bold'))}
                self.labels['Palabras'].grid(row=2, column=0, columnspan=2)
                for pos, palabra in enumerate(sorted(self.palabras)):
                        self.labels[palabra] = Label(self.cuadro_palabras, text=palabra, anchor='w')
                        self.labels[palabra].grid(row=(pos // 2) + (pos % 1) + 3, column=pos % 2, sticky='W')


        #Método que registra los eventos de los botones de la sopa de letras
        def click_evento(self, fila, columna):
                contador=0
                if self.botones[fila][columna].cget('bg') == self.color:
                        self.botones[fila][columna].configure(bg='SystemButtonFace')
                        self.presionado.remove((self.botones[fila][columna].cget('text'), columna, fila))
                else:
                        self.botones[fila][columna].configure(bg=self.color)
                        self.presionado.add((self.botones[fila][columna].cget('text'), columna, fila))
                        for palabra, coordenadas in self.clase_genera_tablero.res.items():
                                #El uso "&" verifica las condiciones como un "and" pero bit por bit
                                if coordenadas & self.presionado == coordenadas:
                                        contador+=1
                                        if contador==len(self.palabras):
                                                self.parartiempo()
                                                messagebox.showinfo(message="You win!", title="State")
                                                return menuVictoriaEnglish(menuDuracion,"duracion",self.segundos,self.largo)
                                        else:
                                                for _, c, f in coordenadas:
                                                        self.botones[f][c].configure(state=DISABLED)
                                                self.labels[palabra].configure(bg=self.color)


        #Método que muestra la solución total de la sopa de letras
        def solucionarTodo(self):
                bg = self.color
                state = DISABLED
                self.parartiempo()
                messagebox.showwarning(message="Game over", title="State")
                self.solucionB.configure(state=state)
                          

                self.verRespuesta = not self.verRespuesta
                for palabra, coordenadas in self.clase_genera_tablero.res.items():
                        self.labels[palabra].configure(bg=bg)
                        for _, c, f in coordenadas:
                                self.botones[f][c].configure(state=state, bg=bg)

        #Función que hace llamada a la clase "FormaPalabra" para formar la cuadrilla a usar del tablero
        #esta a su vez cambia los botones a lo que está en la matriz formada por "FormaPalabra"
        def hacer_tablero(self):

                if self.verRespuesta:
                        self.verRespuesta = not self._solution_shown
                self.clase_genera_tablero = FormaPalabra(self.largo, self.palabras)
                self.presionado.clear()

                for f in range(self.largo):
                        for c in range(self.largo):
                                self.botones[f][c].configure(text=self.clase_genera_tablero.tablero[f][c], bg='SystemButtonFace',state=NORMAL)

                for label in self.labels.values():
                        label.configure(bg='SystemButtonFace')


###########
#############
#Clase juego contrarreloj
class juegoSopaLetrasContrarrelojEnglish:
        def __init__(self,menu,largo,palabras,segundos):
                #Constructor
                menu.destroy()
                global menuContra
                menuContra = Tk()
                menuContra.title('Wordsearch timetrial')
                menuContra.resizable(False, False)
                
                #Frame que contendrá la sopa de letras
                self.cuadrilla_letras = Frame(menuContra)
                #Frame que contendrá las palabras a encontrar
                self.cuadro_palabras = Frame(menuContra)
                #Frame que contendrá los botones volver y mostrar solución
                self.menu = Frame(menuContra)
                #Frame que contendrá el cronómetro
                self.cuadroTiempo=Frame(menuContra)

                self.verRespuesta = False
                self.largo = largo
                self.color = "brown"

                #Cóndiciones de botones al ser presionados
                self.presionado=set()
                self.palabras=palabras
                #Cuadrilla de botones en limpio
                self.botones=[]
                for f in range(self.largo):
                        fila=[]
                        for c in range(self.largo):
                                fila.append(Button(self.cuadrilla_letras,padx=5, command=partial(self.click_evento, f, c)
                                ))
                                fila[-1].grid(row=f, column=c, sticky='ew')
                        self.botones.append(fila)

                #Labels y botones solución y volver
                titulo=Label(self.menu, text='Menu', pady=5, font=('bold')).grid(row=0, column=0, columnspan=2, sticky='ew')
                # Botón de solución
                self.solucionB=Button(self.menu, text='Solution', padx=1, pady=1, command=self.solucionarTodo)
                self.solucionB.grid(row=1, column=0, sticky='ew')
                #Botón de volver al juego
                self.volver = Button(self.menu, text='Return', padx=1, pady=1, command=lambda:self.volverJuego(menuContra)).grid(row=1, column=1, sticky='ew')
                #Label y cronómetro
                tituloTiempo=Label(self.cuadroTiempo, text='Time:', pady=5, font=('bold')).grid(row=0, column=0, columnspan=2, sticky='ew')
                #cronómetro
                
                self.segundos=segundos
                self.crono=Label(self.cuadroTiempo,text="", pady=8, font=('bold'))
                self.crono.grid(row=2, column=0, columnspan=2, sticky='ew')

                self.labels = {}
                self.busqueda_palabra = None
                self.crear_labels()
                self.hacer_tablero()

                #Posiciones de los frames

                self.cuadrilla_letras.pack(side=LEFT)
                self.menu.pack(side=TOP, pady=self.largo)
                self.cuadro_palabras.pack(side=TOP, padx=40, pady=20)
                self.cuadroTiempo.pack(side=TOP, pady=self.largo)
                #Inicia el tiempo
                self.tiempo()
                

                menuContra.mainloop()



        #Métodos
        #Método que registra el tiempo restante que le queda al usuario
        def tiempo(self):
                if self.segundos==0:
                        self.solucionarTodo()
                else:
                        self.segundos=self.segundos-1
                        self.crono.configure(text=str(self.segundos)+ " seconds")
                        self.detener=self.cuadroTiempo.after(1000, self.tiempo)

        #Método que detiene el cronómetro
        def parartiempo(self):
                self.cuadroTiempo.after_cancel(self.detener)
                self.crono.configure(text=str(self.segundos)+ " seconds")

        #Método volver
        def volverJuego(self,menuBasico):
                self.parartiempo()
                return tipoJuegoEnglish(menuBasico)


        #Método que muestra como labels las palabras a jugar
        def crear_labels(self):
                for label in self.labels.values():
                        label.destroy()
                self.labels.clear()
                self.labels = {'Palabras': Label(self.cuadro_palabras, text='Words', pady=5, font=('bold'))}
                self.labels['Palabras'].grid(row=2, column=0, columnspan=2)
                for pos, palabra in enumerate(sorted(self.palabras)):
                        self.labels[palabra] = Label(self.cuadro_palabras, text=palabra, anchor='w')
                        self.labels[palabra].grid(row=(pos // 2) + (pos % 1) + 3, column=pos % 2, sticky='W')


        #Método que registra los eventos de los botones de la sopa de letras
        def click_evento(self, fila, columna):
                contador=0
                if self.botones[fila][columna].cget('bg') == self.color:
                        self.botones[fila][columna].configure(bg='SystemButtonFace')
                        self.presionado.remove((self.botones[fila][columna].cget('text'), columna, fila))
                else:
                        self.botones[fila][columna].configure(bg=self.color)
                        self.presionado.add((self.botones[fila][columna].cget('text'), columna, fila))
                        for palabra, coordenadas in self.clase_genera_tablero.res.items():
                                #El uso "&" verifica las condiciones como un "and" pero bit por bit
                                if coordenadas & self.presionado == coordenadas:
                                        contador+=1
                                        if contador==len(self.palabras):
                                                self.parartiempo()
                                                messagebox.showinfo(message="You win!", title="State")
                                                return menuVictoriaEnglish(menuContra,"contrarreloj",self.segundos,self.largo)
                                        else:
                                                for _, c, f in coordenadas:
                                                        self.botones[f][c].configure(state=DISABLED)
                                                self.labels[palabra].configure(bg=self.color)


        #Método que muestra la solución total de la sopa de letras
        def solucionarTodo(self):
                bg = self.color
                state = DISABLED
                self.parartiempo()
                messagebox.showwarning(message="Game over", title="State")
                self.solucionB.configure(state=state)
                          

                self.verRespuesta = not self.verRespuesta
                for palabra, coordenadas in self.clase_genera_tablero.res.items():
                        self.labels[palabra].configure(bg=bg)
                        for _, c, f in coordenadas:
                                self.botones[f][c].configure(state=state, bg=bg)

        #Función que hace llamada a la clase "FormaPalabra" para formar la cuadrilla a usar del tablero
        #esta a su vez cambia los botones a lo que está en la matriz formada por "FormaPalabra"
        def hacer_tablero(self):

                if self.verRespuesta:
                        self.verRespuesta = not self._solution_shown
                self.clase_genera_tablero = FormaPalabra(self.largo, self.palabras)
                self.presionado.clear()

                for f in range(self.largo):
                        for c in range(self.largo):
                                self.botones[f][c].configure(text=self.clase_genera_tablero.tablero[f][c], bg='SystemButtonFace',state=NORMAL)

                for label in self.labels.values():
                        label.configure(bg='SystemButtonFace')



 #Interfaz que crea nickname y lo guarda en "jugadores.txt"               
def menuVictoriaEnglish(menu,tipoJuego,tiempo,dificultad):
        menu.destroy()
        menuInfoGanador=Tk()
        menuInfoGanador.title("Winner info")  
        menuInfoGanador.geometry("600x300+300+5")
        menuInfoGanador.resizable(False,False)
        menuInfoGanador.config(bg="gray")
        
        #Label de titulo
        titulo=Label(menuInfoGanador,text="Enter your nickname",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=100,y=10)
        #Palabra
        palabra=Label(menuInfoGanador,text="nickname:",bg="#ffffff",fg="black",font=("Stencil","10"),width=("15"),height=("3")).place(x=10,y=80)
        palabraSet=StringVar()
        entradaPalabra=Entry(menuInfoGanador, font=("Stencil",25,'bold'),width=20,textvariable=palabraSet,bg="powder blue", justify="left").place(x=160,y=85)

        #Botones
        Boton1=Button(menuInfoGanador,text="Create",bg="#0B6121",fg="white",font=("Stencil","15"),width=("35"),height=("3"),command=lambda:agregarJugadorEnglish(menuInfoGanador,palabraSet,tipoJuego,tiempo,dificultad))
        Boton1.place(x=65,y=200)

        menuInfoGanador.mainloop()


#Escritura archivos en jugadores.txt
#E:Ventana, palabra,strings y numeros(indicaría el tiempo y dificultad)
#S:Escritura de archivos en jugadores.txt
#R:No deben repetirse nicknames en el modo duración con la misma dificultad
def agregarJugadorEnglish(menuInfoGanador,palabraSet,estiloJuego,tiempo,dificultad):
        nickname=palabraSet.get()
        nickname=nickname.upper()
        if nickname=="" or nickname==" ":
                messagebox.showerror(message="Invalid nickname", title="Error")
        else:
                if estiloJuego=="duracion":
                        if dificultad==12:
                                if seRepiteUsuarioEnglish(nickname,"principiante"):
                                        messagebox.showerror(message="Invalid nickname", title="Error")
                                else:
                                        file=open("players.txt","a")
                                        file.write(nickname+","+estiloJuego+","+"principiante,"+str(tiempo)+"\n")
                                        file.close()
                                        return tipoJuegoEnglish(menuInfoGanador)
                        elif dificultad==20:
                                if seRepiteUsuarioEnglish(nickname,"intermedio"):
                                        messagebox.showerror(message="nickname no válido", title="Error")
                                else:
                                        file=open("players.txt","a")
                                        file.write(nickname+","+estiloJuego+","+"intermedio,"+str(tiempo)+"\n")
                                        file.close()
                                        return tipoJuegoEnglish(menuInfoGanador)
                        elif dificultad==28:
                                if seRepiteUsuarioEnglish(nickname,"avanzado"):
                                        messagebox.showerror(message="nickname no válido", title="Error")
                                else:
                                        file=open("players.txt","a")
                                        file.write(nickname+","+estiloJuego+","+"avanzado,"+str(tiempo)+"\n")
                                        file.close()
                                        return tipoJuegoEnglish(menuInfoGanador)

                else:
                        if dificultad==12:
                                file=open("players.txt","a")
                                file.write(nickname+","+estiloJuego+","+"principiante\n")
                                file.close()
                                return tipoJuegoEnglish(menuInfoGanador)
                        elif dificultad==20:
                                file=open("players.txt","a")
                                file.write(nickname+","+estiloJuego+","+"intermedio\n")
                                file.close()
                                return tipoJuegoEnglish(menuInfoGanador)
                        elif dificultad==28:
                                file=open("players.txt","a")
                                file.write(nickname+","+estiloJuego+","+"avanzado\n")
                                file.close()
                                return tipoJuegoEnglish(menuInfoGanador)




#Verifica que no se repitan usuarios en modalidad de juego "Duración"
#Estos se pueden repetir solo si están en jugabilidades distintas o dificultades diferentes
#Uso de clase validarNickname
def seRepiteUsuarioEnglish(nickname,dificultad):
        verifica=validarNickname("players.txt")
        condicion=verifica.nicknameRepetido(nickname,dificultad)
        if condicion:
                return True
        else:
                return False


                        
                        

#Interfaz de ayuda de juego
def ayudaJuegoEnglish(menu):
        menu.destroy()
        menu_ayuda=Tk()
        menu_ayuda.geometry("500x600+200+65")
        menu_ayuda.resizable(False,False)
        menu_ayuda.title("Wordsearch help")
        menu_ayuda.config(bg="gray")
        titulo = Label(menu_ayuda,text="Info of the game",bg="gray",fg="white",font=('Broadway 25 bold'))
        titulo.place(x=50,y=0)
        Menus=Button(menu_ayuda,text="Main menu",bg="green",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:ayudaMenuPEnglish(menu_ayuda))
        Menus.place(x=85,y=100)
        juegoBasico=Button(menu_ayuda,text="Basic Game",bg="purple",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:ayudaMenuBEnglish(menu_ayuda))
        juegoBasico.place(x=85,y=200)
        juegoDuracion=Button(menu_ayuda,text="Duration Game",bg="blue",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:ayudaMenuDEnglish(menu_ayuda))
        juegoDuracion.place(x=85,y=300)
        juegoContra=Button(menu_ayuda,text="TimeTrial Game",bg="orange",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:ayudaMenuCEnglish(menu_ayuda))
        juegoContra.place(x=85,y=400)
        volver=Button(menu_ayuda,text="Return",bg="red",fg="white",width=20,font=('Helvetica 20 bold'),command=lambda:volver_menuEnglish(menu_ayuda))
        volver.place(x=85,y=500)
        menu_ayuda.mainloop()


#Interfaz e información sobre el uso de "menú principal"
def ayudaMenuPEnglish(menu):
        menu.destroy()
        ayudaMenuPrincipal=Tk()
        ayudaMenuPrincipal.geometry("600x600+300+5")
        ayudaMenuPrincipal.resizable(False,False)
        ayudaMenuPrincipal.title("Information of the program")
        ayudaMenuPrincipal.config(bg="gray")
        #Label de titulo
        titulo=Label(ayudaMenuPrincipal,text="Information of the main menu",bg="gray",fg="white",font=('Broadway 20 bold'))
        titulo.place(x=50,y=10)
        #Widget de textbox
        scroll = Scrollbar(ayudaMenuPrincipal)
        texto = Text(ayudaMenuPrincipal,font =('Helvetica 15 bold'), height=19, width=45)
        scroll.config(command=texto.yview)
        scroll.pack(side=RIGHT, fill="y")
        texto.pack(side=LEFT, fill="y")
        mensaje="""***Main menu***
********************
In this menu the options will be displayed
(selectable with the mouse)
Play, Language, Words,
Help, Statistics and Exit

1-Play: It will display a menu with the
game modes and desired difficulty
-------------
2-Language: Allows change
program language, will be displayed
Spanish and English options
-------------
3-Words: The word bank, this allows
add, modify and delete the words
to be used in the game
-------------
4-Help: This is the section that has the
instructions for use of the program
-------------
5-Statistics: This section will classify
the stored data
in the text file called "players"
this will classify by
the gameplay, then the chosen difficulty
by the player and at the end
will qualify for best time
in the gameplay "duration"
and number of victories in
gameplay "against the clock"
--------------------------------
6-Exit: This section allows you to close the program"""

        texto.insert(END, mensaje)
        texto.config(yscrollcommand=scroll.set)
        texto.config(state='disabled')
        texto.place(x=40, y=55)
        #Boton volver
        volver=Button(ayudaMenuPrincipal,text="Return",bg="red",fg="white",width=25,font=('Helvetica 15 bold'),command=lambda:ayudaJuegoEnglish(ayudaMenuPrincipal))
        volver.place(x=135,y=545)
        ayudaMenuPrincipal.mainloop()

#Interfaz e información sobre el uso de la jugabilidad básica de la sopa de letras
def ayudaMenuBEnglish(menu):
        menu.destroy()
        ayudaMenuJuegoBasico=Tk()
        ayudaMenuJuegoBasico.geometry("600x600+300+5")
        ayudaMenuJuegoBasico.resizable(False,False)
        ayudaMenuJuegoBasico.title("Information of the basic gameplay")
        ayudaMenuJuegoBasico.config(bg="gray")
        #Label de titulo
        titulo=Label(ayudaMenuJuegoBasico,text="Information of the basic gameplay",bg="gray",fg="white",font=('Broadway 17 bold'))
        titulo.place(x=25,y=10)
        #Widget de textbox
        scroll = Scrollbar(ayudaMenuJuegoBasico)
        texto = Text(ayudaMenuJuegoBasico,font =('Helvetica 15 bold'), height=19, width=45)
        scroll.config(command=texto.yview)
        scroll.pack(side=RIGHT, fill="y")
        texto.pack(side=LEFT, fill="y")
        mensaje="""*** Basic gameplay ***
************************
In this menu the game will be displayed with
the basic gameplay, this one does not have time
nor does it save data when you win
the match. Before playing
the player can play with the
words from the word bank
or have the player enter them
manually
In the game will unfold
left the board while
the right has the
following sections:

----------------
1-Show solution: Solve automatically
the words to look for in the soup
letters and indicates the user a message
called "End of the game"

-------------
2-Return: Allows you to return to the section
of "type of game"
that allows to start another game
-------------
3-Words: List of words to be seen
in-game, these will be marked when
found by the player, at the time
find them all
a message will come out
indicating that you have won the game"""

        texto.insert(END, mensaje)
        texto.config(yscrollcommand=scroll.set)
        texto.config(state='disabled')
        texto.place(x=40, y=55)
        #Botón volver
        volver=Button(ayudaMenuJuegoBasico,text="Return",bg="red",fg="white",width=25,font=('Helvetica 15 bold'),command=lambda:ayudaJuegoEnglish(ayudaMenuJuegoBasico))
        volver.place(x=135,y=545)
        ayudaMenuJuegoBasico.mainloop()

#Interfaz e información sobre el uso de la jugabilidad "duración" de la sopa de letras
def ayudaMenuDEnglish(menu):
        menu.destroy()
        ayudaMenuJuegoDuracion=Tk()
        ayudaMenuJuegoDuracion.geometry("600x600+300+5")
        ayudaMenuJuegoDuracion.resizable(False,False)
        ayudaMenuJuegoDuracion.title("Information of the duration gameplay")
        ayudaMenuJuegoDuracion.config(bg="gray")
        #Label de titulo
        titulo=Label(ayudaMenuJuegoDuracion,text="Information of the duration gameplay",bg="gray",fg="white",font=('Broadway 17 bold'))
        titulo.place(x=25,y=10)
        #Widget de textbox
        scroll = Scrollbar(ayudaMenuJuegoDuracion)
        texto = Text(ayudaMenuJuegoDuracion,font =('Helvetica 15 bold'), height=19, width=45)
        scroll.config(command=texto.yview)
        scroll.pack(side=RIGHT, fill="y")
        texto.pack(side=LEFT, fill="y")
        mensaje="""***Gameplay duration ***
************************
In this menu the game will be displayed
with duration gameplay,
this will count the time that lasts
the player to find all the words
in the alphabet soup, before playing
the player can play with the
words from the word bank
or have the player enter them
manually
In the game will unfold
left the board while
the right has the
following sections:
------------------

1-Show solution: Solve
automatically search words
in the alphabet soup
and indicates the user a message
called "End of the game" and
that stops time, by pressing it
it can only be returned, since it equates
to surrender

-------------
2-Return: Allows you to return to the
"game type" section
that allows to start another game
-------------

3-Words: List of words to be seen
in the game
these will be marked when found
by the player, the moment the
find all you will get a message
indicating that you have won the game
and it will take you to a menu that will allow you
enter your nickname and be
registered in the list of
players to see in statistics
-----------------------

4-Stopwatch: Shows the amount
time remaining"""

        texto.insert(END, mensaje)
        texto.config(yscrollcommand=scroll.set)
        texto.config(state='disabled')
        texto.place(x=40, y=55)
        #Botón volver
        volver=Button(ayudaMenuJuegoDuracion,text="Return",bg="red",fg="white",width=25,font=('Helvetica 15 bold'),command=lambda:ayudaJuegoEnglish(ayudaMenuJuegoDuracion))
        volver.place(x=135,y=545)
        ayudaMenuJuegoDuracion.mainloop()

#Interfaz e información sobre el uso de la jugabilidad "contrarreloj" de la sopa de letras
def ayudaMenuCEnglish(menu):
        menu.destroy()
        ayudaMenuJuegoContrarreloj=Tk()
        ayudaMenuJuegoContrarreloj.geometry("600x600+300+5")
        ayudaMenuJuegoContrarreloj.resizable(False,False)
        ayudaMenuJuegoContrarreloj.title("Information of the timetrial gameplay")
        ayudaMenuJuegoContrarreloj.config(bg="gray")
        #Label de titulo
        titulo=Label(ayudaMenuJuegoContrarreloj,text="Information of the TimeTrial gameplay",bg="gray",fg="white",font=('Broadway 17 bold'))
        titulo.place(x=15,y=10)
        #Widget de textbox
        scroll = Scrollbar(ayudaMenuJuegoContrarreloj)
        texto = Text(ayudaMenuJuegoContrarreloj,font =('Helvetica 15 bold'), height=19, width=45)
        scroll.config(command=texto.yview)
        scroll.pack(side=RIGHT, fill="y")
        texto.pack(side=LEFT, fill="y")
        mensaje="""*** Gameplay time trail ***
************************
In this menu the game will be displayed
with gameplay time trail,
this will count the time that will go
decreasing to 0.
By the time you get to
0, will show all words
that were to be found and
will throw the message of
"End of the game", in that
moment the user will only be able to return
to the types of games with the button.
The player must find
all the words before
time is running out on the
alphabet soup, before playing
the player can play with the
words from the word bank
or have the player enter them
manually like
the duration you want of the
stopwatch, which can be
manual or predetermined by
difficulty

1-Show solution: Solve automatically
the words to search in the alphabet soup
and indicates the user a message
called "End of the game" and
that stops time, by pressing it
it can only be returned, since it equates
to surrender
-------------

2-Return: Allows you to return to the section of
"type of game" that lets you start
another different game
------------------

3-Words: List of words to be seen
in the game
these will be marked when found
by the player, the moment the
find all you will get a message
indicating that you have won the game
and it will take you to a menu that will allow you
enter your nickname and be
registered in the list of
players to see in statistics
--------------------------

4-Stopwatch: Shows the amount
time remaining"""

        texto.insert(END, mensaje)
        texto.config(yscrollcommand=scroll.set)
        texto.config(state='disabled')
        texto.place(x=40, y=55)
        #Botón volver
        volver=Button(ayudaMenuJuegoContrarreloj,text="Return",bg="red",fg="white",width=25,font=('Helvetica 15 bold'),command=lambda:ayudaJuegoEnglish(ayudaMenuJuegoContrarreloj))
        volver.place(x=135,y=545)
        ayudaMenuJuegoContrarreloj.mainloop()









                


        
menu()







