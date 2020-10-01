print("--- ADICIONANDO ELEMENTOS EM UM ARRAY ---")

def main():
    registro = []

    while True:
        valores = str(input("Digite algo para adcionar a lista: "))
        registro.append(valores)
        condição = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
        if condição in 'N':
            break
    print("• Itens adicionados a lista: ", registro)

main()