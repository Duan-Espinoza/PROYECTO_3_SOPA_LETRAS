# Clase dificultad de palabras #
from tkinter import messagebox

import random

class dificultadPalabras:
    #Constructor
    def __init__(self,archivo):
        self.archivo=archivo
        

    #Métodos

    #Método leer archivo
    def leerArchivo(self):
        file= open(self.archivo,"r")
        contenido= file.read()
        file.close()
        return (contenido)
    

    #Método para la selección de 6 palabras
    def Principiante(self):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        lista3= self.eliminarRepetidas("",lista2)
        lista4= self.sacarPrincipiante(lista3)
        res=[]
        cont=0

        if self.cantidadPrincipiante()>=6 and lista4!=[]:
            palabra=random.choice(lista4)
            

            while  len(palabra)>=3 and len(palabra)<=12:
                while cont<6:
                    res+= [palabra]
                    lista4= self.eliminarRepetidas(palabra,lista4)
                    cont+=1
                    if lista4==[]:
                        return res
                    else:
                        palabra=random.choice(lista4)  
                    
                
                return res
            
            lista4= self.eliminarRepetidas(palabra,lista4)
            palabra=random.choice(lista4)
        else:
            return messagebox.showerror(message="Palabras insuficientes para la dificultad Principiante", title="Error")
        
        

    #Método para la selección de 10 palabras        
    def Intermedio(self):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        lista3= self.eliminarRepetidas("",lista2)
        lista4= self.sacarIntermedio(lista3)
        res=[]
        cont=0

        if self.cantidadIntermedio()>=10 and lista4!=[]:
            palabra=random.choice(lista4)

            while  len(palabra)>=3 and len(palabra)<=20:
                while cont<10:
                    res+= [palabra]
                    lista4= self.eliminarRepetidas(palabra,lista4)
                    cont+=1
                    if lista4==[]:
                        return res
                    else:
                        palabra=random.choice(lista4)
                        
                
                return res
            
            lista4= self.eliminarRepetidas(palabra,lista4)
            palabra=random.choice(lista4)
        else:
            return messagebox.showerror(message="Palabras insuficientes para la dificultad Intermedio", title="Error")
            
        

    #Método para la selección de 14 palabras
    def Avanzado(self):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        lista3= self.eliminarRepetidas("",lista2)
        lista4= self.sacarAvanzado(lista3)
        res=[]
        cont=0

        if self.cantidadAvanzado()>=14 and lista4!=[]:
            palabra=random.choice(lista4)

            while  len(palabra)>=3 and len(palabra)<=28:
                while cont<14:
                    res+= [palabra]
                    lista4= self.eliminarRepetidas(palabra,lista4)
                    cont+=1
                    if lista4==[]:
                        return res
                    else:
                        palabra=random.choice(lista4)
                
                return res
            
            lista4= self.eliminarRepetidas(palabra,lista4)
            palabra=random.choice(lista4)
        else:
            return messagebox.showerror(message="Palabras insuficientes para la dificultad Avanzado", title="Error")

        
                    
    #Método para evitar casos repetidos
    def eliminarRepetidas(self,palabra,lista):
        res=[]

        for x in lista:
            if x!=palabra:
                res+=[x]
        return res


    #Método validación de cantidad de palabras para principiante

    def cantidadPrincipiante(self):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        res=0

        while lista2!=[]:
            for x in lista2:
                if len(x)>=3 and len(x)<=12:
                    res+=1
            return res

        return messagebox.showerror(message="No hay palabras a contar", title="Error")
        
    

    #Método validación de cantidad de palabras para principiante
    def cantidadIntermedio(self):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        res=0

        while lista2!=[]:
            for x in lista2:
                if len(x)>=3 and len(x)<=20:
                    res+=1
            return res

        return messagebox.showerror(message="No hay palabras a contar", title="Error")
        
    
    #Método validación de cantidad de palabras para avanzado
    def cantidadAvanzado(self):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        res=0

        while lista2!=[]:
            for x in lista2:
                if len(x)>=3 and len(x)<=28:
                    res+=1
            return res

        return messagebox.showerror(message="No hay palabras a contar", title="Error")




    
        
    #Saca las palabras que cumplan condición de "principiante" 
    def sacarPrincipiante(self,lista):
        res=[]

        for x in lista:
            if len(x)<=12:
                res+=[x]
        return res


        
    #Saca las palabras que cumplan condición de "Intermedio"
    def sacarIntermedio(self,lista):
        res=[]

        for x in lista:
            if len(x)<=20:
                res+=[x]
        return res

    
    #Saca las palabras que cumplan condición de "avanzado"
    def sacarAvanzado(self,lista):
        res=[]

        for x in lista:
            if len(x)<=28:
                res+=[x]
        return res

    

#########################
##########################
#Inglés
class dificultadPalabras2:
    #Constructor
    def __init__(self,archivo):
        self.archivo=archivo
        

    #Métodos

    #Método leer archivo
    def leerArchivo(self):
        file= open(self.archivo,"r")
        contenido= file.read()
        file.close()
        return (contenido)
    

    #Método para la selección de 6 palabras
    def Principiante(self):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        lista3= self.eliminarRepetidas("",lista2)
        lista4= self.sacarPrincipiante(lista3)
        res=[]
        cont=0

        if self.cantidadPrincipiante()>=6 and lista4!=[]:
            palabra=random.choice(lista4)
            

            while  len(palabra)>=3 and len(palabra)<=12:
                while cont<6:
                    res+= [palabra]
                    lista4= self.eliminarRepetidas(palabra,lista4)
                    cont+=1
                    if lista4==[]:
                        return res
                    else:
                        palabra=random.choice(lista4)  
                    
                
                return res
            
            lista4= self.eliminarRepetidas(palabra,lista4)
            palabra=random.choice(lista4)
        else:
            return messagebox.showerror(message="Not enough word for difficulty Easy", title="Error")
        
        

    #Método para la selección de 10 palabras        
    def Intermedio(self):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        lista3= self.eliminarRepetidas("",lista2)
        lista4= self.sacarIntermedio(lista3)
        res=[]
        cont=0

        if self.cantidadIntermedio()>=10 and lista4!=[]:
            palabra=random.choice(lista4)

            while  len(palabra)>=3 and len(palabra)<=20:
                while cont<10:
                    res+= [palabra]
                    lista4= self.eliminarRepetidas(palabra,lista4)
                    cont+=1
                    if lista4==[]:
                        return res
                    else:
                        palabra=random.choice(lista4)
                        
                
                return res
            
            lista4= self.eliminarRepetidas(palabra,lista4)
            palabra=random.choice(lista4)
        else:
            return messagebox.showerror(message="Not enough words for dificulty medium", title="Error")
            
        

    #Método para la selección de 14 palabras
    def Avanzado(self):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        lista3= self.eliminarRepetidas("",lista2)
        lista4= self.sacarAvanzado(lista3)
        res=[]
        cont=0

        if self.cantidadAvanzado()>=14 and lista4!=[]:
            palabra=random.choice(lista4)

            while  len(palabra)>=3 and len(palabra)<=28:
                while cont<14:
                    res+= [palabra]
                    lista4= self.eliminarRepetidas(palabra,lista4)
                    cont+=1
                    if lista4==[]:
                        return res
                    else:
                        palabra=random.choice(lista4)
                
                return res
            
            lista4= self.eliminarRepetidas(palabra,lista4)
            palabra=random.choice(lista4)
        else:
            return messagebox.showerror(message="Not enough words for dificulty hard", title="Error")

        
                    
    #Método para evitar casos repetidos
    def eliminarRepetidas(self,palabra,lista):
        res=[]

        for x in lista:
            if x!=palabra:
                res+=[x]
        return res


    #Método validación de cantidad de palabras para principiante

    def cantidadPrincipiante(self):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        res=0

        while lista2!=[]:
            for x in lista2:
                if len(x)>=3 and len(x)<=12:
                    res+=1
            return res

        return messagebox.showerror(message="There´s not words for easy", title="Error")
        
    

    #Método validación de cantidad de palabras para principiante
    def cantidadIntermedio(self):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        res=0

        while lista2!=[]:
            for x in lista2:
                if len(x)>=3 and len(x)<=20:
                    res+=1
            return res

        return messagebox.showerror(message="There´s not words for medium", title="Error")
        
    
    #Método validación de cantidad de palabras para avanzado
    def cantidadAvanzado(self):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        res=0

        while lista2!=[]:
            for x in lista2:
                if len(x)>=3 and len(x)<=28:
                    res+=1
            return res

        return messagebox.showerror(message="There´s not word for hard", title="Error")




    
        
    #Saca las palabras que cumplan condición de "principiante" 
    def sacarPrincipiante(self,lista):
        res=[]

        for x in lista:
            if len(x)<=12:
                res+=[x]
        return res


        
    #Saca las palabras que cumplan condición de "Intermedio"
    def sacarIntermedio(self,lista):
        res=[]

        for x in lista:
            if len(x)<=20:
                res+=[x]
        return res

    
    #Saca las palabras que cumplan condición de "avanzado"
    def sacarAvanzado(self,lista):
        res=[]

        for x in lista:
            if len(x)<=28:
                res+=[x]
        return res










        
        
        

        
    
