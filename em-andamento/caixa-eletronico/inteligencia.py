import time

programa_situacao = True
notas_sucesso = [[200, 2], [100, 4], [50, 10], [20, 15], [10, 20], [5, 25], [2, 7]]
notas_temporarias = [[200, 2], [100, 4], [50, 10], [20, 15], [10, 20], [5, 25], [2, 7]]


soma_caixa = notas_sucesso[0][0]*notas_sucesso[0][1] + notas_sucesso[1][0]*notas_sucesso[0][1] + notas_sucesso[2][0]*notas_sucesso[0][1] + notas_sucesso[3][0]*notas_sucesso[0][1] + notas_sucesso[4][0]*notas_sucesso[5][1]+ notas_sucesso[6][0]*notas_sucesso[0][1]

while programa_situacao == True:
    notas_recebidas = [[200, 0], [100, 0], [50, 0], [20, 0], [10, 0], [5, 0], [2, 0]]
    cx = 'CAIXA ELETRÔNICO'
    print('-='*20)
    print(f'\033[1;34;40m{cx:^40}\033[m')
    print('-='*20)
    transacao = str(input("[0] - Saque \n[1] - Depósito \n[999] - Finalizar \nEscolha uma opção: ")).strip()

    if transacao == '0' or transacao == '1' or transacao == '999':
        if transacao == '0':
            saque = str(input('Quanto você quer sacar? ').strip())
            saque_temporario = saque

            if saque[-1] == '1' or saque[-1] == '3':
                print('Nossos caixas só aceitam valores com o último dígito diferente de 1 e 3.')
                decisao = ''
                while decisao != 'S' or decisao != 'N':
                    decisao = str(input('Deseja fazer mais transações? [\033[32;40mS\033[m/\033[31;40mN\033[m] ')).strip().upper()
                    if decisao == 'N':
                        print('Volte sempre.')
                        programa_situacao = False
                        break

                    elif decisao == 'S':
                        break

            elif soma_caixa < int(saque):

                print('Valor indisponível nesse caixa')
                decisao = str(input('Deseja fazer mais transações? [\033[32;40mS\033[m/\033[31;40mN\033[m] ')).strip().upper()
                if decisao == 'N':
                    print('Volte sempre.')
                    programa_situacao = False
                    break

                elif decisao == 'S':
                    break
            
            elif soma_caixa > int(saque):
                
                #VALIDAÇÃO
                transacao_realizada = True
                for c in range(len(notas_temporarias)):
                    while int(notas_temporarias[c][1]) != 0 and (int(saque_temporario) >= int(notas_temporarias[c][0])):
                        if int(notas_temporarias[c][1]) > 0: 
                            saque_temporario = int(saque_temporario) - int(notas_temporarias[c][0])
                            notas_temporarias[c][1] = int(notas_temporarias[c][1]) - 1
                            transacao_realizada = True
                        
                    if int(saque_temporario) == 0:
                        transacao_realizada = True
                        break
                        
                    if int(notas_temporarias[c][1]) == 0:
                        transacao_realizada = False

                if transacao_realizada == False:
                    print('\033[30;41mSAQUE NÃO REALIZADO\033[m. Motivo: Falta de notas.')
                
                elif transacao_realizada == True:
                    for c in range(len(notas_sucesso)):
                        
                        auxiliar = ''
                        while int(notas_sucesso[c][1]) != 0 and (int(saque) >= int(notas_sucesso[c][0])):
                            if int(notas_sucesso[c][1]) > 0: 
                                saque = int(saque) - int(notas_sucesso[c][0])
                                notas_sucesso[c][1] = int(notas_sucesso[c][1]) - 1

                                for g in range(len(notas_recebidas)):
                                    if notas_recebidas[g][0] == notas_sucesso[c][0]:
                                        notas_recebidas[g][1] = int(notas_recebidas[g][1]) + 1
                    
                    if int(saque) == 0:
                            print('\033[30;42mSAQUE REALIZADO\033[m')
                            print('-='*20)
                            aux = 'Notas e suas respectivas Quantidades:'
                            print(f'\033[1;30;40m{aux:^40}\033[m')
                            for k, c in notas_recebidas:
                                if c != 0:
                                    print(f'Notas de R$ {k}.00: {c} Cédulas.')
                               
                decisao = ''
                while decisao != 'S' or decisao != 'N' :
                    decisao = str(input('Deseja fazer mais transações? [\033[32;40mS\033[m/\033[31;40mN\033[m] ')).strip().upper()
                    if decisao == 'N':
                        print('Volte sempre.')
                        programa_situacao = False
                        break

                    elif decisao == 'S':
                        break

        if transacao == '1':
            print('\033[1;31;40mEM CONSTRUÇÃO.\033[m Escolha outra opção. ')

        if transacao == '999':
            print('Finalizando todas as transações...')
            time.sleep(1)
            print('Volte sempre!')
            break

    #ERRO DE DIGITAÇÃO DO USUÁRIO
    else:
        print('\033[30;41m OPÇÃO INVÁLIDA!\033[m tente novamente.')
