from abc import ABC, abstractmethod

class Ciclista(ABC):
    
    def __init__(self, identificador, nombre):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__tiempo_acumulado = 0 
    @abstractmethod
    def imprimir_tipo(self):
        pass 
    def get_identificador(self):
        return self.__identificador

    def set_identificador(self, identificador):
        self.__identificador = identificador

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_Posición_general(self, Posición_general):
        self.__Posición_general = Posición_general
    
    def get_Posición_general(self):
        return self.__Posición_general
    
    def get_tiempo_acumulado(self):
        return self.__tiempo_acumulado

    def set_tiempo_acumulado(self, tiempo):
        self.__tiempo_acumulado = tiempo
    
    def imprimir(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"Equipo: {self.__equipo}")
        print(f"Tiempo acumulado: {self.__tiempo_acumulado}")