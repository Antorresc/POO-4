class Equipo:
    def __init__(self, nombre, pais):
        self.__nombre = nombre 
        self.__pais = pais
        self.lista_ciclistas = [] 
        self.total_tiempo = 0.0
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_pais(self):
        return self.__pais
    
    def set_pais(self, pais):
        self.__pais = pais
        
    def agregar_ciclista(self, ciclista):
        self.lista_ciclistas.append(ciclista) #append funciona para agregar al final de la lista
        
    def listar_equipo(self):
        print("Ciclistas en el equipo:")
        for ciclista in self.lista_ciclistas:
            print(ciclista.get_nombre())
            
    def buscar_ciclista(self, nombre_ciclista):
        for ciclista in self.lista_ciclistas:
            if ciclista.get_nombre() == nombre_ciclista:
                return ciclista
        return f"Ciclista con nombre {nombre_ciclista} no encontrado."
    
    def calcular_total_tiempo(self):
        self.total_tiempo = sum(ciclista.get_tiempo_acumulado() for ciclista in self.lista_ciclistas)
        
    def imprimir_datos_equipo(self):
        self.calcular_total_tiempo() 
        print(f"Nombre del equipo = {self.__nombre}")
        print(f"País = {self.__pais}")
        print(f"Tiempo total acumulado del equipo: {self.total_tiempo} minutos")

        