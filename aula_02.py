def ordena_tres_numeros(valor1, valor2, valor3):
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1
    if valor2 > valor3:
        valor2, valor3 = valor3, valor2
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1
    print(valor1, valor2, valor3)


def ordena_tres_numeros_alt(valores):
    if valores[0] > valores[1]:
        valores[0], valores[1] = valores[1], valores[0]
    if valores[1] > valores[2]:
        valores[1], valores[2] = valores[2], valores[1]
    if valores[0] > valores[1]:
        valores[0],valores[1] = valores[1], valores[0]
    print(valores[0], valores[1], valores[2])


def decompoe_numero(valor):
    print("oi", valor % 10)
    print((valor // 10) % 10)
    print(valor // 100)

# "%" serve para ver o que sobra da divisão -> 4 % 2 = 0 -> 4 dividido por 2 é 2 e sobra 0
# "//" serve para ver o número inteiro da divisão -> 5 // 2 = 2 -> 5 dividido por 2 é 2,5 que inteiro é 2


def e_mult(valor, divisor):
    if (valor % divisor == 0):
        print(valor, "é um múltiplo de", divisor,'.')
    else:
        print(valor, "não é um múltiplo de", divisor,'.')



def informa_pares():
    for i in range(2):
        valor = int(input('Insira um número:'))
        e_mult(valor, 2)


def informa_maior():
    maximo = 0
    for i in range(2):
        valor = int(input("Insira um número: "))
        if valor > maximo:
            maximo = valor
    print("O maior valor inserido é", maximo)

def informa_maior_alt():
    numero = []
    for i in range(3):
        numero.append(int(input("Informe um valor: ")))
    print(max(numero))


def main():
    informa_maior_alt()


if __name__ == "__main__":
    main()


