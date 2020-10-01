print("--- POSITIVO OU NEGATIVO ---")

def main():
    numero = float(input("Digite um número: "))
    if numero > 0:
        print("O número {} é POSITIVO.".format(numero))
    elif numero < 0:
        print("O número {} é NEGATIVO.".format(numero))
    else:
        print("O número informado é ZERO.")

main()