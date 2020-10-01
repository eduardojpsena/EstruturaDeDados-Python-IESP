print("--- TEMPO NA FILA ---")

def mainFor():
    print("• Programa em laço for iniciado •")
    numClientes = int(input("Digite o número de clientes na sua frente: "))

    tempoTotal = 0
    if numClientes <= 5:
        for c in range(0, numClientes):
            tempoEspera = float(input("Digite o tempo de espera do cliente na {}° Posição (min): ".format(c+1)))
            tempoTotal += tempoEspera

        tempoMedio = tempoTotal / numClientes
        print("O tempo médio de espera na fila é de: {:.2f} minutos".format(tempoMedio))
    else:
        print("Número de clientes no banco utrapassou o limite permitido.")

def mainWhile():
    print("• Programa em laço while iniciado •")
    numClientes = int(input("Digite o número de clientes na sua frente: "))

    tempoTotal = 0
    contador = 0
    if numClientes <= 5:
        while (contador < numClientes):
            tempoEspera = float(input("Digite o tempo de espera do cliente na {}° Posição (min): ".format(contador+1)))
            tempoTotal += tempoEspera
            contador += 1

        tempoMedio = tempoTotal / numClientes
        print("O tempo médio de espera na fila é de: {:.2f} minutos".format(tempoMedio))
    else:
        print("Número de clientes no banco utrapassou o limite permitido.")

mainFor()
mainWhile()