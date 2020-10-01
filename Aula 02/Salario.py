print("---SALARIO---")

def salarioBruto(salarioHora, horasMes):
    return salarioHora * horasMes

def irrf(brutoMes):
    return brutoMes * (11/100)

def inss(brutoMes):
    return brutoMes * (8/100)

def sindicato(brutoMes):
    return brutoMes * (5/100)

def main():
    nome = str(input("Digite seu nome: "))
    matricula = int(input("Digite sua matricula: "))
    salarioHora = float(input("Informe sua remuneração por hora: R$ "))
    horasMes = float(input("Horas trabalhadas no mês (hrs.min): "))
    salarioBrutoMes = salarioBruto(salarioHora, horasMes)
    valorDescontado = irrf(salarioBrutoMes) + inss(salarioBrutoMes) + sindicato(salarioBrutoMes)
    salarioLiquido = salarioBrutoMes - valorDescontado

    print("\n••••••••••••••••••••••EXTRATO••••••••••••••••••••••".format())
    print("Nome: {} - Matricula: {}".format(nome, matricula))
    print("►Proventos◄")
    print("Salário Bruto: R$ {:.2f}".format(salarioBrutoMes))
    print("►Descontos◄")
    print("IPRF: R$ {:.2f} - INSS: R$ {:.2f} - Sindicato: R$ {:.2f}".format(irrf(salarioBrutoMes),
                                                inss(salarioBrutoMes),sindicato(salarioBrutoMes)))
    print("Total descontos: R$ {:.2f}".format(valorDescontado))
    print("\nSalário liquido: R$ {:.2f}".format(salarioLiquido))
main()
