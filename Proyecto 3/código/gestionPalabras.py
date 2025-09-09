from tkinter import messagebox
#Clase gestión de palabras 
class gestionPalabras:
    #Constructor

    def __init__(self,archivo):
        self.archivo= archivo

    #Métodos

    #Lectura archivos
    def leerArchivo(self):
        file= open(self.archivo,"r")
        contenido= file.read()
        file.close()
        return (contenido)

    #Escritura archivos
    def agregarContenido(self,contenido):
        file= open(self.archivo,"a")
        file.write(contenido)
        file.close()

    #Agregar palabra
    def agregarPalabra(self,palabra):
        if isinstance (palabra,str) and palabra!="" and len(palabra)<=28 and len(palabra)>=3:
            lista= self.leerArchivo()
            lista2= lista.split("\n")

            while lista2!=[]:
                
                for x in lista2:
                    if x==palabra:
                        return messagebox.showerror(message="La palabra ya existe", title="Error")
                agregar=self.agregarContenido(palabra+"\n")
                return messagebox.showinfo(message="La palabra se ha agregada con éxito", title="Estado")
            
            agregar=self.agregarContenido(palabra+"\n")
            return messagebox.showinfo(message="La palabra se ha agregada con éxito", title="Estado")
        
        else:
            return messagebox.showerror(message="Parámetros de ingreso no válidos", title="Error")


    #Modificar palabra

    def modificarPalabra(self,palabra,cambio):
        if isinstance (palabra,str) and isinstance(cambio,str) and cambio!="" and len(cambio)<=28 and len(cambio)>=3:
            if self.validaPalabra(cambio):
                return messagebox.showerror(message="La palabra ya existe en el banco de palabras", title="Error")
            
            elif self.validaPalabra(palabra):
                res=""
                lista= self.leerArchivo()
                lista2= lista.split("\n")

                while lista2!=[]:
                    for x in lista2:
                        if x==palabra:
                            res+=(cambio+"\n")
                        else:
                            res+=(x+"\n")
                    file= open(self.archivo,"w")
                    file.write(res)
                    file.close()
                    return messagebox.showinfo(message="La palabra ha sido modificada con éxito", title="Estado")

                return messagebox.showerror(message="No hay palabras en el banco de palabras", title="Error")

            else:
                return messagebox.showerror(message="La palabra por modificar no existe", title="Error")
        else:
            return messagebox.showerror(message="La palabra por modificar es inválida", title="Error")
            
            

    #Modificar palabra
    def validaPalabra(self,palabra):
        lista= self.leerArchivo()
        lista2= lista.split("\n")

        for x in lista2:
            if x==palabra:
                return True
            
        return False

    #Eliminar palabra
    def eliminarPalabra(self,palabra):
        if isinstance (palabra,str) and palabra!="":
            if self.validaPalabra(palabra):
                lista= self.leerArchivo()
                lista2= lista.split("\n")
                res=""

                for x in lista2:
                    if x != palabra:
                        res += (x + "\n")
                file= open(self.archivo,"w")
                file.write(res)
                file.close()
                return messagebox.showinfo(message="La palabra ha sido eliminada con éxito", title="Estado")

            else:
                return messagebox.showerror(message="La palabra por eliminar no existe en el banco de palabras", title="Error")

        else:
            return messagebox.showerror(message="Debe ingresar una cadena de texto", title="Error")

##################################
#Inglés
#Clase gestión de palabras 
class gestionPalabras2:
    #Constructor

    def __init__(self,archivo):
        self.archivo= archivo

    #Métodos

    #Lectura archivos
    def leerArchivo(self):
        file= open(self.archivo,"r")
        contenido= file.read()
        file.close()
        return (contenido)

    #Escritura archivos
    def agregarContenido(self,contenido):
        file= open(self.archivo,"a")
        file.write(contenido)
        file.close()

    #Agregar palabra
    def agregarPalabra(self,palabra):
        if isinstance (palabra,str) and palabra!="" and len(palabra)<=28 and len(palabra)>=3:
            lista= self.leerArchivo()
            lista2= lista.split("\n")

            while lista2!=[]:
                
                for x in lista2:
                    if x==palabra:
                        return messagebox.showerror(message="The word already exist", title="Error")
                agregar=self.agregarContenido(palabra+"\n")
                return messagebox.showinfo(message="The word has been added", title="State")
            
            agregar=self.agregarContenido(palabra+"\n")
            return messagebox.showinfo(message="The word has been added", title="State")
        
        else:
            return messagebox.showerror(message="The entry parameters are no allowed", title="Error")


    #Modificar palabra

    def modificarPalabra(self,palabra,cambio):
        if isinstance (palabra,str) and isinstance(cambio,str) and cambio!="" and len(cambio)<=28 and len(cambio)>=3:
            if self.validaPalabra(cambio):
                return messagebox.showerror(message="The word already exist", title="Error")
            
            elif self.validaPalabra(palabra):
                res=""
                lista= self.leerArchivo()
                lista2= lista.split("\n")

                while lista2!=[]:
                    for x in lista2:
                        if x==palabra:
                            res+=(cambio+"\n")
                        else:
                            res+=(x+"\n")
                    file= open(self.archivo,"w")
                    file.write(res)
                    file.close()
                    return messagebox.showinfo(message="The word has been successfully modified", title="Estado")

                return messagebox.showerror(message="The word doesnt exist", title="Error")

            else:
                return messagebox.showerror(message="The word doesnt exist", title="Error")
        else:
            return messagebox.showerror(message="The word are not allowed", title="Error")
            
            

    #Modificar palabra
    def validaPalabra(self,palabra):
        lista= self.leerArchivo()
        lista2= lista.split("\n")

        for x in lista2:
            if x==palabra:
                return True
            
        return False

    #Eliminar palabra
    def eliminarPalabra(self,palabra):
        if isinstance (palabra,str) and palabra!="":
            if self.validaPalabra(palabra):
                lista= self.leerArchivo()
                lista2= lista.split("\n")
                res=""

                for x in lista2:
                    if x != palabra:
                        res += (x + "\n")
                file= open(self.archivo,"w")
                file.write(res)
                file.close()
                return messagebox.showinfo(message="The word has been deleted", title="State")

            else:
                return messagebox.showerror(message="The word doesnt exist", title="Error")

        else:
            return messagebox.showerror(message="You have to enter a text", title="Error")

    
                
                
        










                
            
            
                
        
        
        
    
