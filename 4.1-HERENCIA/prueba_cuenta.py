from cuenta_ahorros import CuentaAhorros

def main():
    print("Cuenta de ahorros")
    saldo_inicial = float(input("Ingrese saldo inicial: $"))
    tasa_interes = float(input("Ingrese tasa de interés: "))
    cuenta = CuentaAhorros(saldo_inicial, tasa_interes)

    cantidad_depositar = float(input("Ingresar cantidad a consignar: $"))
    cuenta.consignar(cantidad_depositar)

    cantidad_retirar = float(input("Ingresar cantidad a retirar: $"))
    cuenta.retirar(cantidad_retirar)

    cuenta.extracto_mensual()
    cuenta.imprimir()

if __name__ == "__main__":
    main()
