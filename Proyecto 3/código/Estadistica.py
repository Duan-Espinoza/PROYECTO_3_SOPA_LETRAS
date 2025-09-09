#Clase para sacar estadisticas #

class Estadistica:
    # Constructor #
    def __init__(self,archivo):
        self.archivo= archivo
        
    # Leer archivos #
    def leerArchivo(self):
        file= open(self.archivo,"r")
        contenido= file.read()
        file.close()
        return (contenido)

    # La uso para eliminar "" #
    def eliminarRepetidas(self,palabra,lista):
        res=[]

        for x in lista:
            if x!=palabra:
                res+=[x]
        return res

    # La uso para eliminar un elemento de la lista #
    def eliminarLista(self,elemento,lista):
        res=[]

        for x in lista:
            if x!=elemento:
                res+=[x]
        return res

    # Sacar menor tiempo de la lista #

    def menorTiempo(self,tipo,dificultad,lista):
        comparador=0
        res=""

        for x in lista:
            partes=x.split(",")
            if comparador==0:
                if partes[2]==dificultad and partes[1]==tipo:
                    comparador=partes[3]
                    res=[x]
            else:
                if partes[2]==dificultad and partes[1]==tipo:
                    if comparador>partes[3]:
                        comparador=partes[3]
                        res=[x]
        return res

    # Sacar estadistica según tipo y dificultad #

    def obtenerEstadisticas(self,tipo,dificultad):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        lista3= self.eliminarRepetidas("",lista2)
        res=[]
        if tipo=="duracion":
            
            while len(res)<3:
                dato= self.menorTiempo(tipo,dificultad,lista3)
                nuevaLista= self.eliminarLista(dato[0],lista3)
                res+= dato
                lista3= nuevaLista
            

            return res
        
        else:

            while len(res)<3:
                dato= self.mayorVictorias(tipo,dificultad,lista3)
                dato2= dato[0][:len(dato)-3]
                nuevaLista= self.eliminarLista(dato2,lista3)
                res+=dato
                lista3= nuevaLista
                
            return res
                

    # Ordena las estadisticas para mejor entendimiento #

    def ordenarEstadisticas(self,tipo,dificultad):
        if tipo=="duracion":
            res=""
            puesto=1
            lista= self.obtenerEstadisticas(tipo,dificultad)

            for x in lista:
                partes= x.split(",")
                nombre= partes[0]
                tiempo= partes[3]

                res+= "PUESTO "+str(puesto)+": "+nombre+", "+"RECORD: "+tiempo+" SEGUNDOS\n"
                puesto+=1

            return res

        else:
            res=""
            puesto=1
            lista= self.obtenerEstadisticas(tipo,dificultad)

            for x in lista:
                partes= x.split(",")
                nombre= partes[0]
                ganadas= partes[3]

                res+= "PUESTO "+str(puesto)+": "+nombre+", "+"RECORD: "+ganadas+" VICTORIAS\n"
                puesto+=1

            return res

            

    # Sacar cantidad de victorias #

    def sacarVictorias(self,nombre,tipo,dificultad,lista):
        res=0

        for x in lista:
            partes= x.split(",")
            if partes[0]==nombre and dificultad==partes[2] and tipo==partes[1]:
                res+=1

        return res

    # Obtiene el participante con mas juegos ganados según tipo y dificultad #

    def mayorVictorias(self,tipo,dificultad,lista):
        comparador=0
        res=0

        for x in lista:
            partes=x.split(",")
            if comparador==0:
                if dificultad==partes[2] and tipo==partes[1]:
                    comparador= self.sacarVictorias(partes[0],tipo,dificultad,lista)
                    res=[x+","+str(comparador)]
            else:
                if dificultad==partes[2] and tipo==partes[1]:
                    if comparador< self.sacarVictorias(partes[0],tipo,dificultad,lista):
                        comparador= self.sacarVictorias(partes[0],tipo,dificultad,lista)
                        res=[x+","+str(comparador)]

        return res

    # Ver totales según el tipo de juego #

    def verTotal(self,tipo):
            p= self.ordenarEstadisticas(tipo,"principiante")
            i= self.ordenarEstadisticas(tipo,"intermedio")
            a= self.ordenarEstadisticas(tipo,"avanzado")

            return str("PRINCIPIANTE:\n"+p+"*****************************\n"+"INTERMEDIO:\n"+i+"*****************************\n"+"AVANZADO:\n"+a+"*****************************")



############
##########
#Versión inglés
class Estadistica2:
    # Constructor #
    def __init__(self,archivo):
        self.archivo= archivo
        
    # Leer archivos #
    def leerArchivo(self):
        file= open(self.archivo,"r")
        contenido= file.read()
        file.close()
        return (contenido)

    # La uso para eliminar "" #
    def eliminarRepetidas(self,palabra,lista):
        res=[]

        for x in lista:
            if x!=palabra:
                res+=[x]
        return res

    # La uso para eliminar un elemento de la lista #
    def eliminarLista(self,elemento,lista):
        res=[]

        for x in lista:
            if x!=elemento:
                res+=[x]
        return res

    # Sacar menor tiempo de la lista #

    def menorTiempo(self,tipo,dificultad,lista):
        comparador=0
        res=""

        for x in lista:
            partes=x.split(",")
            if comparador==0:
                if partes[2]==dificultad and partes[1]==tipo:
                    comparador=partes[3]
                    res=[x]
            else:
                if partes[2]==dificultad and partes[1]==tipo:
                    if comparador>partes[3]:
                        comparador=partes[3]
                        res=[x]
        return res

    # Sacar estadistica según tipo y dificultad #

    def obtenerEstadisticas(self,tipo,dificultad):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        lista3= self.eliminarRepetidas("",lista2)
        res=[]
        if tipo=="duracion":
            
            while len(res)<3:
                dato= self.menorTiempo(tipo,dificultad,lista3)
                nuevaLista= self.eliminarLista(dato[0],lista3)
                res+= dato
                lista3= nuevaLista
            

            return res
        
        else:

            while len(res)<3:
                dato= self.mayorVictorias(tipo,dificultad,lista3)
                dato2= dato[0][:len(dato)-3]
                nuevaLista= self.eliminarLista(dato2,lista3)
                res+=dato
                lista3= nuevaLista
                
            return res
                

    # Ordena las estadisticas para mejor entendimiento #

    def ordenarEstadisticas(self,tipo,dificultad):
        if tipo=="duracion":
            res=""
            puesto=1
            lista= self.obtenerEstadisticas(tipo,dificultad)

            for x in lista:
                partes= x.split(",")
                nombre= partes[0]
                tiempo= partes[3]

                res+= "RANK "+str(puesto)+": "+nombre+", "+"RECORD: "+tiempo+" SECONDS\n"
                puesto+=1

            return res

        else:
            res=""
            puesto=1
            lista= self.obtenerEstadisticas(tipo,dificultad)

            for x in lista:
                partes= x.split(",")
                nombre= partes[0]
                ganadas= partes[3]

                res+= "RANK "+str(puesto)+": "+nombre+", "+"RECORD: "+ganadas+" WINS\n"
                puesto+=1

            return res

            

    # Sacar cantidad de victorias #

    def sacarVictorias(self,nombre,tipo,dificultad,lista):
        res=0

        for x in lista:
            partes= x.split(",")
            if partes[0]==nombre and dificultad==partes[2] and tipo==partes[1]:
                res+=1

        return res

    # Obtiene el participante con mas juegos ganados según tipo y dificultad #

    def mayorVictorias(self,tipo,dificultad,lista):
        comparador=0
        res=0

        for x in lista:
            partes=x.split(",")
            if comparador==0:
                if dificultad==partes[2] and tipo==partes[1]:
                    comparador= self.sacarVictorias(partes[0],tipo,dificultad,lista)
                    res=[x+","+str(comparador)]
            else:
                if dificultad==partes[2] and tipo==partes[1]:
                    if comparador< self.sacarVictorias(partes[0],tipo,dificultad,lista):
                        comparador= self.sacarVictorias(partes[0],tipo,dificultad,lista)
                        res=[x+","+str(comparador)]

        return res

    # Ver totales según el tipo de juego #

    def verTotal(self,tipo):
            p= self.ordenarEstadisticas(tipo,"principiante")
            i= self.ordenarEstadisticas(tipo,"intermedio")
            a= self.ordenarEstadisticas(tipo,"avanzado")

            return str("EASY:\n"+p+"*****************************\n"+"MEDIUM:\n"+i+"*****************************\n"+"HARD:\n"+a+"*****************************")

    
                        
                
        
                
    
        
                    
                
                

        














    
