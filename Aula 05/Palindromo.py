print("--- DETECTOR DE PALÍNDROMO ---")

def funcaoPalindromo(valorTemp):
    numerosInvertidos = ""
    for c in range(len(valorTemp) - 1, 0 - 1, -1):
        numerosInvertidos += valorTemp[c]
    return numerosInvertidos

def main():
    numeros = str(input("Digite uma sequência de números para verificar se é palíndromo: "))
    if numeros == funcaoPalindromo(numeros):
        print("A sequência de números é um palíndromo")
    else:
        print("A sequência de números não é um palíndromo")

main()