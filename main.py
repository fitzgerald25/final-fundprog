from datetime import date
import os
from datetime import timedelta
import numpy_financial as npf
import tabulate as tab

class CalculadoraPrestamos:
    Monto: float
    Plazo: int
    Tasa: float
    Cuota: float

    def CuotaMensual(self, monto, plazo, tasa):
        cuota = float(round(npf.pmt(tasa, plazo, -monto, 0), 0))
        return cuota

    def MostrarTabla(self, monto, plazo, tasa, cuota):
        os.system('cls')
        print("Usted está simulando un crédito con las siguientes características: ")
        print(f"Monto del préstamo en RD$: \t\t\t\t{monto}")
        print(f"Tasa del Porcentaje Anual: \t\t\t\t{tasa}")
        print(f"Plazo (cuotas en meses): \t\t\t\t{plazo}")
        print(f"Valor de la Cuota: \t\t\t\t{cuota}")
        print("*********************************************************************\n*********************************************************************")
        #print("Pago\tFechas de Pago\tCuota\tCapital\tInterés\tBalance")
        datos = []
        fecha = date.today()
        capital = float(0)
        balance = float(monto)

        for k in range(1, plazo+1):
            #print(f"{k+1}\t\t{fecha}\t\t{cuota}\t{capital}\t{interes}\t{balance}")
            capital = npf.ppmt(tasa, k, plazo, -monto, 0)
            interes = cuota - capital
            balance -= capital
            linea = [k, fecha, format(cuota, '0,.0f'), format(capital, '0,.0f'), format(interes, '0,.0f'), format(balance, '0,.0f')]
            datos.append(linea)
            fecha += timedelta(days=30)
        print(tab.tabulate(datos, headers=['Pago', 'Fechas', 'Cuota', 'Capital', 'Interes', 'Balance']))

def main():
    print("********CALCULADORA DE PRÉSTAMOS**********")
    print("******************************************")
    calculadora = CalculadoraPrestamos()
    calculadora.Monto = float(input("Escriba el monto: "))
    calculadora.Plazo = int(input("Escriba el plazo (cantidad de cuotas en meses): "))
    calculadora.Tasa = (float(input("Escriba la tasa de interés (de 0-100): ")))*0.01
    calculadora.Cuota = calculadora.CuotaMensual(calculadora.Monto, calculadora.Plazo, calculadora.Tasa)
    calculadora.MostrarTabla(calculadora.Monto, calculadora.Plazo, calculadora.Tasa, calculadora.Cuota)

if __name__ == '__main__':
    main()