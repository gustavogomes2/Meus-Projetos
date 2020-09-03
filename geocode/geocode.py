import geopandas as gpds
import pandas as pds # Para carregar a planilha com os endereços

ler = pds.read_excel(r'C:\Users\Gustavo Gomes\Documents\Programação\Meus-Projetos\Geocode\geocode dados.xlsx')
#print(ler) plota a tabela
ler2 = gpds.tools.geocode(ler['UF2'], provider = 'nominatim', user_agent="Intro Geocode")

#MELHORAR O ALGORITMO AFIM DE PULAR ERROS DE PESQUISA, QUANDO ACONTECER.

c = 'DADOS: QUANTIDADE DE ALUNOS EM CADA CIDADE'
print('-=-'*20)
print(f'{c:-^70}')
print(ler)

b = 'LATITUDE'
print(f'{b:-^70}')
lista = str(ler2['geometry'].y).split()
for i in range(len(lista)-1):
    if i%2 == 1:
        print(lista[i])     
        
a = 'LONGITUDE'
print(f'{a:-^70}')
lista = str(ler2['geometry'].x).split()
for i in range(len(lista)-1):
    if i%2 == 1:
        print(lista[i])