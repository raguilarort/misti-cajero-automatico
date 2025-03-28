import math
from datetime import datetime
import platform
import os
import time

class ATM:

    def __init__(self, banco, ubicacion, total_efectivo):
        self.banco = banco
        self.ubicacion = ubicacion
        self.total_efectivo = total_efectivo

    #region MÉTODOS IMPRESIÓN MENÚS

    # Mensaje bienvenida
    def bienvenida(self):
        print('*********************************************')
        print('***    BIENVENIDA (O) AL CAJERO AUTOMÁTICO ', self.banco, '***********')
        print('Por favor inicia sesión para hacer uso de todas las funcionalidades')
        print('*********************************************')

    # Menú principal
    def menu_principal(self, cliente):
        print('******** Cajero Automático de ', self.banco, ' Sucursal ', self.ubicacion, ' ********\n')
        if cliente.sexo == "Hombre":
            print('Bienvenid@ ', cliente.nombre, ' indica la operación que deseas realizar\n')
        print('1. Consultar saldo\n')
        print('2. Retirar Efectivo\n')
        print('3. Depositar Efectivo\n')
        print('4. Pagar algún servicio\n')
        print('0. Cerrar sesión\n')

    def menu_pago_servicio(self):
        print('******** Módulo para pagar los servicios ********\n')
        print('Por favor selecciona la opción que coincida con el servicio que deseas pagar')
        print('1. Luz (CFE)\n')
        print('2. Gas (Flamagas)\n')
        print('3. Teléfono (izzi, totalplay, telmex)\n')
        print('4. Telefonía (Telcel)\n')
        print('0. Regresar\n')

    def limpiar_pantalla(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
    #endregion


    #region MÉTODOS GESTIÓN INFORMACIÓN CLIENTE
    def iniciar_sesion(self, cliente, usuario, contrasena):
        if cliente.usuario == usuario and cliente.password == contrasena :
            return True
        else:
            return False

    # Control para consultar saldo
    def modulo_consultar_saldo(self, cliente):
        self.limpiar_pantalla()
        print('********** Consultar Saldo **********\n')
        print("{:^20} {:^30} {:^30}".format('Banco', 'Tipo Cuenta', 'Saldo Disponible'))
        for cuenta in cliente.cuentas_bancarias:
            print("{:<20} {:<30} {:<30}".format(cuenta.banco, cuenta.tipo_cuenta_bancaria, cuenta.saldo_disponible))

    # Control para retirar efectivo
    def modulo_retirar_efectivo(self, cliente):
        self.limpiar_pantalla()
        print('********** Retirar Efectivo **********\n')

        try:
            monto_retirar = int(input('Introduce la cantidad que deseas retirar: '))

            if self.total_efectivo > monto_retirar:
                if cliente.cuentas_bancarias[0].saldo_disponible >= monto_retirar:
                    self.total_efectivo -= monto_retirar
                    cliente.cuentas_bancarias[0].saldo_disponible -= monto_retirar
                    print("Ya puesdes tomar tu efectivo en la badeja.\n\n")
                    print("Tu saldo actual es: ", cliente.cuentas_bancarias[0].saldo_disponible)
                else:
                    print('Saldo insuficiente en la cuenta ', cliente.cuentas_bancarias[0].tipo_cuenta_bancaria)
            else:
                print("Lo sentimos, el cajero no cuenta con el importe que quieres solicitar")
        except ValueError:
            print("Por favor introduce un importe válido.")
            time.sleep(1)

    # Control para depositar efectivo. SOBRECARGA
    def modulo_depositar_efectivo(self, cliente, **kwargs):
        self.limpiar_pantalla()
        print('********** Depositar Efectivo **********\n')

        try:
            monto_depositar = kwargs.get("monto")
            if monto_depositar is None:
                monto_depositar = int(input('Introduce la cantidad que estás depositando: '))
            
            descripcion = kwargs.get("descripcion")
            if descripcion is None:
                descripcion = input('Introduce una descripción para el depósito: ')

            if monto_depositar > 0:
                self.total_efectivo += monto_depositar
                cliente.cuentas_bancarias[0].saldo_disponible += monto_depositar
                
                print("Tu dinero se abonó con éxito.\n")
                print("Descripción: ", descripcion)
                print("Tu saldo actual es: ", cliente.cuentas_bancarias[0].saldo_disponible)

        except ValueError:
            print("Por favor introduce un importe válido.")
            time.sleep(1)

    @staticmethod
    def pagar_servicio(cliente, empresa, contrato, importe):
        if cliente.cuentas_bancarias[0].saldo_disponible >= importe:
            cliente.cuentas_bancarias[0].saldo_disponible -= importe
            print("El pago se realizó con éxito. A continuación, te comparto tu ticket.\n\n")
            print("Empresa: ", empresa)
            print("Contrato: ", contrato)
            print("Importe pagado: ", importe)
            print("Fecha y hora de la operación: ", datetime.now())
            raiz_cuadrada = math.sqrt(25)
            print(raiz_cuadrada)
        else:
            print('Saldo insuficiente en la cuenta ', cliente.cuentas_bancarias[0].tipo_cuenta_bancaria)

'''
    def modulo_pagar_servicios(self, cliente):

        self.limpiar_pantalla()

        try:
            opcion_principal = int(input('Opción: '))

            match opcion_principal:
                case 1:
                    self.limpiar_pantalla()
                    contrato = input("Ingresa el número de contrato que tienes con CFE: ")
                    importe = int(input("Ingresa la cantidad que deseas pagar: "))

                    ATM.pagar_servicio(cliente, 'CFE', contrato, importe)
                case 2:
                    self.limpiar_pantalla()
                    contrato = input("Ingresa el número de contrato que tienes con Flamagas: ")
                    importe = int(input("Ingresa la cantidad que deseas pagar: "))

                    ATM.pagar_servicio(cliente, 'Flamagas', contrato, importe)
                case 3:
                    self.limpiar_pantalla()
                    contrato = input("Ingresa el número de contrato que tienes con el proveedor de Internet y/o Teléfono: ")
                    importe = int(input("Ingresa la cantidad que deseas pagar: "))

                    ATM.pagar_servicio(cliente, 'izzi', contrato, importe)
                case 4:
                    self.limpiar_pantalla()
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
'''
    #endregion

