text1 = 'SIMULADOR DE JUROS COMPOSTO'
print('-'*30)
print(f'{text1:^30}')
print('-'*30)

while True:
    tempodeaplicacao = int(input('Quantos anos irá durar: '))
    cont = (idade - idadefinal)*12
    valorinicial = float(input('Preciso do quanto você quer começar aplicar: '))
    parcelas = float(input('Qual o valor da parcela mensal? '))
    porcentagem = float(input('Qual o juros aplicado no montante por ano? em porcentagem '))

    formula = valorinicial*((1-porcentagem)^cont)

    print(formula)
