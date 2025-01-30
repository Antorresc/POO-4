from cuenta import Cuenta

class CuentaAhorros(Cuenta):
    """
    Subclase de Cuenta que representa una cuenta de ahorros con un estado
    de activación basado en el saldo.
    """
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self.activa = saldo >= 10000

    def retirar(self, cantidad: float):
        """Sobrescribe el método retirar para validar si la cuenta está activa."""
        if self.activa:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        """Sobrescribe el método consignar para validar si la cuenta está activa."""
        if self.activa:
            super().consignar(cantidad)

    def extracto_mensual(self):
        """Genera un extracto mensual y aplica condiciones específicas."""
        if self.numero_retiros > 4:
            self.comision_mensual += (self.numero_retiros - 4) * 1000
        super().extracto_mensual()
        self.activa = self.saldo >= 10000

    def imprimir(self):
        """Imprime la información de la cuenta."""
        print(f"Saldo = $ {self.saldo}")
        print(f"Comisión mensual = $ {self.comision_mensual}")
        print(f"Número de transacciones = {self.numero_consignaciones + self.numero_retiros}\n")
