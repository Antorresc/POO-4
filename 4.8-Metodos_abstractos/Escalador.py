from Ciclista import Ciclista

class Escalador(Ciclista):
    
    def __init__(self, identificador, nombre, aceleración_promedio, grado_rampa):
        super().__init__(identificador, nombre)
        self.aceleración_promedio = aceleración_promedio
        self.grado_rampa = grado_rampa
    
    def get_aceleración_promedio(self):
        return self.aceleración_promedio

    def set_aceleración_promedio(self, aceleración_promedio):
        self.aceleración_promedio = aceleración_promedio

    def get_grado_rampa(self):
        return self.grado_rampa

    def set_grado_rampa(self, grado_rampa):
        self.grado_rampa = grado_rampa
        
    def imprimir(self):
        super().imprimir()
        print(f"Aceleración promedio = {self.aceleración_promedio}")
        print(f"Grado de rampa = {self.grado_rampa}")
       
    def imprimir_tipo(self):
        return "Es un escalador"