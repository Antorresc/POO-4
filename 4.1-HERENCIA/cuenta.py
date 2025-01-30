class Cuenta:
    """
    Clase que modela una cuenta bancaria con atributos como saldo, número
    de consignaciones, retiros, tasa anual de interés y comisión mensual.
    """
    def __init__(self, saldo: float, tasa_anual: float):
        self.saldo = saldo
        self.numero_consignaciones = 0
        self.numero_retiros = 0
        self.tasa_anual = tasa_anual
        self.comision_mensual = 0

    def consignar(self, cantidad: float):
        """Método que incrementa el saldo con una cantidad consignada."""
        self.saldo += cantidad
        self.numero_consignaciones += 1

    def retirar(self, cantidad: float):
        """Método que decrementa el saldo si la cantidad no excede el saldo actual."""
        nuevo_saldo = self.saldo - cantidad
        if nuevo_saldo >= 0:
            self.saldo = nuevo_saldo
            self.numero_retiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcular_interes(self):
        """Método que calcula el interés mensual en base a la tasa anual."""
        tasa_mensual = self.tasa_anual / 12
        interes_mensual = self.saldo * tasa_mensual
        self.saldo += interes_mensual

    def extracto_mensual(self):
        """Método que aplica comisión mensual y calcula los intereses."""
        self.saldo -= self.comision_mensual
        self.calcular_interes()
