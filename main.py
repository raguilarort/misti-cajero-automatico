from model.atm import ATM
from model.cliente import Cliente
from model.cuenta_bancaria import CuentaBancaria

import platform
import os
import time
#AUOR920813AAA, ricardo.ao, rick1234
cliente_ricardo = Cliente('Ricardo', 'Aguilar', 'Ortega', 'AUOR920813AAA', 'AUOR920813HDFGPA03', 'Hombre','13/08/1992', 'ESIME CULHUACAN BLA BLA', '000033', '5570248659', '5540657833', 'ricardo.aguilar@gmail.com', 'Spiderman', 'ricardo.ao', 'rick1234')

cliente_ricardo.agregar_cuenta_bancaria(CuentaBancaria('BBVA', 'Cuenta de Débito', 100000))
cliente_ricardo.agregar_cuenta_bancaria(CuentaBancaria('BBVA', 'Cuenta de Ahorro', 200000))
cliente_ricardo.agregar_cuenta_bancaria(CuentaBancaria('BBVA', 'Cuenta de Cheques', 5000))

cliente_luzma = Cliente('Luz Ma', 'XXXXX', 'XXXX', 'LZMA920813XXX', 'LZMA920813XXXMDFGPA01', 'Mujer','01/02/1992', 'ESIME CULHUACAN BLA BLA', '000034', '55702481234', '5540651234', 'luz.ma@gmail.com', 'Batman', 'luz.ma', 'luz1234')

cliente_luzma.agregar_cuenta_bancaria(CuentaBancaria('BBVA', 'Cuenta de Débito', 10000))
cliente_luzma.agregar_cuenta_bancaria(CuentaBancaria('BBVA', 'Cuenta de Ahorro', 20000))
cliente_luzma.agregar_cuenta_bancaria(CuentaBancaria('BBVA', 'Cuenta de Cheques', 500))

cliente_sara = Cliente('Sara', 'YYYYY', 'YYYY', 'SARA920813YYY', 'SARA920813XXXMDFGPA01', 'Mujer','01/03/1992', 'ESIME CULHUACAN BLA BLA', '000035', '55702485678', '5540655678', 'sara@gmail.com', 'Superman', 'sara', 'sara1234')

cliente_sara.agregar_cuenta_bancaria(CuentaBancaria('BBVA', 'Cuenta de Débito', 100000))
cliente_sara.agregar_cuenta_bancaria(CuentaBancaria('BBVA', 'Cuenta de Ahorro', 200000))
cliente_sara.agregar_cuenta_bancaria(CuentaBancaria('BBVA', 'Cuenta de Cheques', 5000))

cliente_uriel = Cliente('Uriel Erandi', 'ZZZZ', 'ZZZZZ', 'URER920813ZZZ', 'URER920813HDFGPA01', 'Hombre','01/02/1992', 'ESIME CULHUACAN BLA BLA', '000036', '55702484321', '5540654321', 'uriel.erandi@gmail.com', 'Hulk', 'uriel.erandi', 'uri1234')

cliente_uriel.agregar_cuenta_bancaria(CuentaBancaria('BBVA', 'Cuenta de Débito', 10000))
cliente_uriel.agregar_cuenta_bancaria(CuentaBancaria('BBVA', 'Cuenta de Ahorro', 20000))
cliente_uriel.agregar_cuenta_bancaria(CuentaBancaria('BBVA', 'Cuenta de Cheques', 500))

clientes_banco = {}  # Se inicializa el diccionario
clientes_banco['AUOR920813AAA'] = cliente_ricardo
clientes_banco['LZMA920813XXX'] = cliente_luzma
clientes_banco['SARA920813YYY'] = cliente_sara
clientes_banco['URER920813ZZZ'] = cliente_uriel


def limpiar_pantalla():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


# Función main
def main():
    cajero = ATM("BBVA", "ESIME-Culhuacan", 100000)

    while True:
        limpiar_pantalla()
        cajero.bienvenida()
        rfc = input("Ingresa tu RFC: ")

        if len(rfc) > 0:
            cliente = clientes_banco.get(rfc)

            if cliente is not None:
                user = input("Ingresa tu Usuario: ")
                password = input("Ingresa tu Contraseña: ")

                if len(user) > 0 and len(password) > 0:
                    if cajero.iniciar_sesion(cliente, user, password) :
                        while True:
                            limpiar_pantalla()
                            cajero.menu_principal(cliente)

                            try:
                                opcion_principal = int(input('Opción: '))

                                match opcion_principal:
                                    case 1:
                                        cajero.modulo_consultar_saldo(cliente)
                                    case 2:
                                        cajero.modulo_retirar_efectivo(cliente)
                                    case 3:
                                        cajero.modulo_depositar_efectivo(cliente)
                                    case 4:
                                        cajero.menu_pago_servicio()
                                        #cajero.modulo_pagar_servicios(cliente)
                                        try:
                                            opcion_principal = int(input('Opción: '))

                                            match opcion_principal:
                                                case 1:
                                                    limpiar_pantalla()
                                                    contrato = input("Ingresa el número de contrato que tienes con CFE: ")
                                                    importe = int(input("Ingresa la cantidad que deseas pagar: "))

                                                    ATM.pagar_servicio(cliente, 'CFE', contrato, importe)
                                                case 2:
                                                    limpiar_pantalla()
                                                    contrato = input("Ingresa el número de contrato que tienes con Flamagas: ")
                                                    importe = int(input("Ingresa la cantidad que deseas pagar: "))

                                                    ATM.pagar_servicio(cliente, 'Flamagas', contrato, importe)
                                                case 3:
                                                    limpiar_pantalla()
                                                    contrato = input("Ingresa el número de contrato que tienes con el proveedor de Internet y/o Teléfono: ")
                                                    importe = int(input("Ingresa la cantidad que deseas pagar: "))

                                                    ATM.pagar_servicio(cliente, 'izzi', contrato, importe)
                                                case 4:
                                                    limpiar_pantalla()
                                                    contrato = input("Ingresa el número de contrato que tienes con el proveedor de Telefonía: ")
                                                    importe = int(input("Ingresa la cantidad que deseas pagar: "))

                                                    ATM.pagar_servicio(cliente, 'Telcel', contrato, importe)
                                                case 0:
                                                    pass
                                                case _:
                                                    print('Opción inválida')
                                                    time.sleep(1)
                                        except ValueError:
                                            print("Por favor introduce un valor válido.")
                                            time.sleep(2)
                                    case 0:
                                        print('Gracias por utilizar nuestro cajero, recoje tu tarjeta al finalizar.')
                                        print('Cerrando sesión...')
                                        break
                                    case _:
                                        print('Opción inválida')
                                        time.sleep(1)
                            except ValueError:
                                print("Por favor introduce un valor válido.")
                                time.sleep(1)
                    else:
                        print("Las credenciales introducidas no coinciden. Vuelve a intentarlo.")
                else:
                    print("Los campos no pueden ir vacíos por favor vuelve a intentarlo.")
        else:
            print('El RFC es indispensable para que puedas iniciar sesión')

        rfc = ""
        user = ""
        password = ""


# Se invoca funcion main()
if __name__ == '__main__':
    main()