print("--- MULTIPLICANDO VALORES DE UM ARRAY ---")

def main():
    numeros = [0, 1, 2, 3, 4]
    for item in range(len(numeros)):
        print("{} x 4 = {}".format(numeros[item], numeros[item] * 4))

main()