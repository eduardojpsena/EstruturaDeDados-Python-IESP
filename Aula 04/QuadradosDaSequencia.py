print("--- QUADRADOS DA SEQUÊNCIA NUMÉRICA ---")

def mainFor():
    print("• Programa em laço for iniciado •")

    inicio = int(input("Digite o n° de inicio da sequência: "))
    fim = int(input("Digite o n° de fim da sequência: "))

    print("Sequência: ", end="")
    for c in range(inicio, fim):
        print(c**2, end=", ")
    print((fim)**2)

def mainWhile():
    print("\n• Programa em laço while iniciado •")

    inicio = int(input("Digite o n° de inicio da sequência: "))
    fim = int(input("Digite o n° de fim da sequência: "))

    print("Sequência: ", end="")
    while (inicio < fim):
        print(inicio ** 2, end=", ")
        inicio += 1
    print((fim)**2)

mainFor()
mainWhile()