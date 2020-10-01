print("---FUNÇÕES---")

def function1(num1, num2):

    return (num1 * 2) * (num2 / 2)

def function2(num1, num3):

    return (num1 * 2) + num3

def function3(num3):

    return num3 ** 3

def main():

    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    num3 = float(input("Digite um número real: "))

    print("•• ({} x 2) x ({} / 2) = {}".format(num1, num2, function1(num1, num2)))
    print("•• ({} x 2) + {} = {}".format(num1, num3, function2(num1, num3)))
    print("•• {}³ = {}".format(num3, function3(num3)))

main()
