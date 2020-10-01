print("--- CONFERINDO GÊNERO ---")

def main():
    genero = str(input("Informe seu gênero [M - Masculino / F - Feminino]: ")).title().strip()

    if genero[0] == "M":
        print("O gênero informado MASCULINO.")
    elif genero[0] == "F":
        print("O gênero informado é FEMININO.")
    else:
        print("Gênero informado INVÁLIDO.")

main()