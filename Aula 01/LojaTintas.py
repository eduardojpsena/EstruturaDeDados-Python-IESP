print("---CALCULO POR ÁREA---")
from math import trunc

area = float(input("Informe a área a ser pintada (m²): "))
quantidade_tinta = area / 3
quantidade_latas = quantidade_tinta / 18

if trunc(quantidade_latas) - quantidade_latas < 0:
    quantidade_latas = trunc(quantidade_latas) + 1

valor_gasto = quantidade_latas * 80

print("O valor total a ser gasto com tinta para a área de {} m² é de R$ {:.2f}.".format(area, valor_gasto))