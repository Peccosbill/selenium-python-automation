class Matematica:

    def sumar(self, nro1, nro2):
        try:
            if nro1 < 0:
                raise Exception('Los números tienen que ser positivos')
        except:
            return 'No puede poner números negativos'
        else:
            return nro1 + nro2

    def restar(self, nro1, nro2):
        return nro1 - nro2

    def multiplicar(self, nro1, nro2):
        try:
            if not type(nro1) is int:
                raise TypeError('Solo enteros')
        except TypeError:
            return('No se puede multiplicar')
        else:
            return nro1 * nro2

    def dividir(self, nro1, nro2):
        n1 = nro1 - 5
        n2 = nro2 - 3
        n3 = 0.0
        try:
            return n1 / n2
        except ZeroDivisionError:
            return 'No se puede dividir por cero'
        except TypeError:
            return 'Debe ingresar números'
        finally:
            print('Hola, quiero dividir')


mi_calculadora = Matematica()

print(mi_calculadora.dividir(4, 2))
print(mi_calculadora.sumar(4, 4))
print(mi_calculadora.sumar(-1, 4))
print(mi_calculadora.multiplicar(1.5, 4))
