print("---CÁLCULOS ARITMÉTICOS---")
horas_trabalhadas = int(input("Quantas horas foram trabalhadas no mês: "))
salario_hora = float(input("Quando você recebe por hora trabalhada: "))

salario_total = horas_trabalhadas * salario_hora

print("Seu salário neste mês é de R$ {}.".format(salario_total))