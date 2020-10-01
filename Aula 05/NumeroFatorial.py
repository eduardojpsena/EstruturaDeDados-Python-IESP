print("--- FATORIAL DE UM NUMERO ---")

def funcaoFatorialFor(valorTemp):
    fatorial = 1
    print("{}! ".format(valorTemp), end="= ")
    for i in range(valorTemp, 1, -1):
        print(i, end=" x ")
        fatorial *= i
    return fatorial
def funcaoFatorialWhile(valorTemp):
    fatorial = 1
    cont = valorTemp
    print("{}! ".format(valorTemp), end="= ")
    while (cont != 1):
        fatorial *= cont
        print(cont, end=" x ")
        cont -= 1
    return fatorial

def main():
    n = int(input("Digite um número inteiro e positivo para calcular seu fatorial: "))
    laco = "for"
    if (n == 0):
        print("0! = 1")
    elif (n >= 1):
        print("• Laço for iniciado •")
        print("1 = {}".format(funcaoFatorialFor(n)))
        print("• Laço while iniciado •")
        print("1 = {}".format(funcaoFatorialFor(n)))
    else:
        print("Número informado é negativo, tente novamente")
        main()

main()

