from Inmuebles import Inmueble
from InmuebleVivienda import InmuebleVivienda
from Apartamento import Apartamento
from Apartaestudio import Apartaestudio
from Apartamento_Familiar import ApartamentoFamiliar
from Casa import Casa
from Casa_Independiente import CasaIndependiente
from Casa_rural import CasaRural
from Casa_Urbana import CasaUrbana
from Casa_ConCerrado import CasaConjuntoCerrado
from Local import Local
from Local_Comercial import LocalComercial
from Oficina import Oficina

def main():
    # Crear un Apartamento Familiar
    apto1 = ApartamentoFamiliar(
        identificadorInmobiliario=103067,
        área=120,
        dirección="Avenida Santander 45-45",
        númeroHabitaciones=3,
        númeroBaños=2,
        valorAdministración=200000
    )
    apto1.calcular_precioVenta(apto1._valorArea)
    print("Datos del Apartamento Familiar:")
    apto1.mostrar_resultados()

    # Crear un Apartaestudio
    aptestudio1 = Apartaestudio(
        identificadorInmobiliario=12354,
        área=50,
        dirección="Avenida Caracas 30-15"
    )
    aptestudio1.calcular_precioVenta(aptestudio1._valorArea)
    print("Datos del Apartaestudio:")
    aptestudio1.mostrar_resultados()
main()
