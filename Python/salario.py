import random
datas = []

for _ in range(20):
    mes = int(random.uniform(1,12))
    dia = int(random.uniform(1,31))
    datas.append('2021-{mes:02d}-{dia:02d}')

from datetime import datetime as dt


def calculaSalario(datas):
    salario = 0
    for data in datas:
        objetoDt = dt.strptime(data, '%Y-%m-%d')
        diaSemana = objetoDt.weekday()
        if diaSemana ==5 or diaSemana==6:
            salario += 30
        else:
            salario += 20
    return salario