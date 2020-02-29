var1 = 50
var2 = 100

conta = (var1 + var2) * var1

print(conta)


def faz_conta():
    return 0

print(faz_conta())

def oi():
    print('oi')

def soma_dois_valores(valor1, valor2):
    return valor1 + valor2

oi()

def raiz_quadrada(gustavo):
    return gustavo ** (1/2)

def raiz(valor, base):
    return valor ** (1/base)

x = soma_dois_valores(3,4)
print(x)
x = soma_dois_valores(2,8)
print(x)

y = raiz_quadrada(9)
print(y)

z = raiz(8, 3)
print(z)

def e_par(valor4):
    return(valor4 % 2) == 0

def div_por_seis(valor5):
    return ((valor5 % 2) == 0) and ((valor5 % 3) == 0)

def testes():
    print(e_par(6))
    print(e_par(5))
    print(div_por_seis(7))
    print(div_por_seis(9))
    print(div_por_seis(12))

def teste_par():
    """Lê um valor inserido pelo usuário, verifica se o valor é par e retorna"""
    parada = False
    while parada == False:
        valor = input('Insira um valor numérico, ou aperte ENTER para encerrar: ')
        if valor == '':
            parada = True
        elif e_par(int(valor)) == True:
            print('O valor inserido é par.')
        else:
            print('O valor inserido é ímpar.')

teste_par()


def dez_mult_tres():
    """a"""
    cont = 0
    numero = 1
    while cont < 10:
        if numero % 3 == 0:
            print(numero)
            cont += 1
            numero += 1
        numero = numero + 1

dez_mult_tres()
