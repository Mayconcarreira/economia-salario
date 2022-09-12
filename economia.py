salario_mensal = float(input('Digite o valor do seu sálario mensal: '))

gasto_mensal = float(input('Digite o valor do seu gasto mensal: '))

salario_total = salario_mensal *  12
gasto_total = gasto_mensal * 12

montante_economizado = salario_total - gasto_total
print('O montante que você economizou ao fim do ano foi: ', montante_economizado)
