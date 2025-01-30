from cuenta import Cuenta

class CuentaCorriente(Cuenta):
    """
    Subclase de Cuenta que representa una cuenta corriente con un atributo
    adicional para el sobregiro.
    """
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self.sobregiro = 0

    def retirar(self, cantidad: float):
        """Sobrescribe el método retirar para manejar el sobregiro."""
        resultado = self.saldo - cantidad
        if resultado < 0:
            self.sobregiro += -resultado
            self.saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        """Sobrescribe el método consignar para reducir el sobregiro si existe."""
        if self.sobregiro > 0:
            residuo = self.sobregiro - cantidad
            if residuo > 0:
                self.sobregiro = residuo
            else:
                self.sobregiro = 0
                self.saldo += -residuo
        else:
            super().consignar(cantidad)

    def imprimir(self):
        """Imprime la información de la cuenta."""
        print(f"Saldo = $ {self.saldo}")
        print(f"Cargo mensual = $ {self.comision_mensual}")
        print(f"Número de transacciones = {self.numero_consignaciones + self.numero_retiros}")
        print(f"Valor de sobregiro = $ {self.sobregiro}\n")
