import folium
from folium.plugins import Fullscreen
from folium.plugins import MarkerCluster
import pandas as pds

#IMPORTANDO A PLANILHA COM DADOS
ler = pds.read_excel(r'C:\Users\Gustavo Gomes\Documents\Programação\Meus-Projetos\Mapa Interativo\test2.xlsx') 

#MAPA: CONFIGURAÇÕES GERAIS
mapa = folium.Map(
    location = [-13.7048968, -69.6590157],
    tiles = 'OpenStreetMap',
    zoom_start = 4,
)

#BOTÃO DE FULLSCREEN
Fullscreen(
    position = 'topright',
    title = 'Entrar/Sair da Tela Cheia',
    title_cancel = 'Sair da Tela Cheia',
    force_separate_button=True).add_to(mapa)


#BOTÃO DE CONTROLE "ESTADOS"
#folium.LayerControl().add_to(mapa)
   
#INTERAÇÕES ENTRE OS MARCADORES.
for index, linha in ler.iterrows():
    
cluster = MarkerCluster(name='UF').add_to(mapa)     
cluster2 = MarkerCluster(name='BRASÍLIA').add_to(mapa)
cluster3 = MarkerCluster(name='OUTROS').add_to(mapa)

print(ler)
#CRIANDO O LOOP
for index, linha in ler.iterrows():
    folium.Marker(location=[linha['LATC'], linha['LONGC']], popup = linha['UF']).add_to(cluster)

#INTERAÇÕES ENTRE OS MARCADORES.

#folium.CircleMarker(location=[-23.8641866,-46.4303154], radius=25, popup='<b>SANTOS</b>', color='#3186cc', fill=True, fill_color='#3186cc').add_to(cluster)

mapa.save('mapa.html')