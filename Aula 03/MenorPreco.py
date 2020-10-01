print("---MENOR PREÇO ---")

def main ():
    menorValor = 100000
    contadorProduto = 0
    for i in range(0, 3):
        produto = float(input("Digite o preço do {}° produto: ".format(i+1)))

        if produto < menorValor:
            menorValor = produto
            contadorProduto = i + 1
    print("O produto {} possui o menor valor, compre-o".format(contadorProduto))

main()