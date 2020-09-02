import folium
from folium.plugins import Fullscreen
from folium.plugins import MarkerCluster
import pandas as pds

#IMPORTANDO A PLANILHA COM DADOS
ler = pds.read_excel(r'C:\Users\Gustavo Gomes\Documents\Programação\Meus-Projetos\Mapa Interativo\Long e Alt - Cidades\arquivtest.xlsx')

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

#INTERAÇÕES ENTRE OS MARCADORES.
cluster = MarkerCluster(name='SÃO PAULO').add_to(mapa)     
cluster2 = MarkerCluster(name='BRASÍLIA').add_to(mapa)
cluster3 = MarkerCluster(name='OUTROS').add_to(mapa)

#MARCADOR
folium.Marker(location = [-15.7750837,-48.0772776], popup = '<b>MARCADOR<\b>',icon = folium.Icon(color='blue', icon='info-sign')).add_to(cluster2) 

#CRIANDO O LOOP

#folium.CircleMarker(location=[-23.8641866,-46.4303154], radius=25, popup='<b>SANTOS</b>', color='#3186cc', fill=True, fill_color='#3186cc').add_to(cluster)

#BOTÃO DE CONTROLE "ESTADOS"
folium.LayerControl().add_to(mapa)

#HTML: SALVAR ARQUIVO
mapa.save('mapa.html')