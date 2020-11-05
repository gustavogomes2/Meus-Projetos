import pandas as pds 

planilha = pds.read_excel(r'C:\Users\Gustavo Gomes\Documents\Programação\Meus-Projetos\Extraindo Dados\exp1 dados.xlsx')

print(planilha)

    for c,n in enumerate(planilha):
        print(c,n)