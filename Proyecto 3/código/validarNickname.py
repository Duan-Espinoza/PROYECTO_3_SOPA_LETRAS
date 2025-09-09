# Clase para validar nicknames #

class validarNickname:
    # Constructor #
    def __init__(self,archivo):
        self.archivo= archivo
        
    # Leer archivos #
    def leerArchivo(self):
        file= open(self.archivo,"r")
        contenido= file.read()
        file.close()
        return (contenido)
    
    # True si es repetido, False si no #
    def nicknameRepetido(self,nickname,dificultad):
        lista= self.leerArchivo()
        lista2= lista.split("\n")
        lista3= self.eliminarRepetidas("",lista2)
        res=0

        for x in lista3:
            partes=x.split(",")
            if partes[2]==dificultad and partes[0]==nickname:
                res+=1
        if res>0:
            return True
        else:
            return False


    # Usada para eliminar "" #
    def eliminarRepetidas(self,palabra,lista):
        res=[]

        for x in lista:
            if x!=palabra:
                res+=[x]
        return res
        
