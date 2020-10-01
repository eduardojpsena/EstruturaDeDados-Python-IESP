print("--- SITUAÇÃO DO ALUNO ---")

def main():
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    media = (nota1 + nota2) / 2

    if media == 10:
        print("Aluno APROVADO COM DISTINÇÃO com média:",media)
    elif media >= 7:
        print("Aluno APROVADO com média:", media)
    else:
        print("Aluno REPROVADO com média:", media)

main()