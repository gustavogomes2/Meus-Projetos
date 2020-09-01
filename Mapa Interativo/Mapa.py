import folium
from folium.plugins import Fullscreen
from folium.plugins import MarkerCluster

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

#DADOS
folium.Marker(location = [-15.7750837,-48.0772776], popup = '3',icon = folium.Icon(color='blue', icon='info-sign')).add_to(cluster2) 
folium.Marker(location = [-23.1119265,-47.2646612], popup = '15',icon = folium.Icon(color='blue', icon='info-sign')).add_to(cluster)
folium.Marker(location = [-2.5606303,-44.3281622], popup = '40',icon = folium.Icon(color='blue', icon='info-sign')).add_to(cluster3)
folium.Marker(location = [-22.7146204,-47.6918722], popup = '3',icon = folium.Icon(color='blue', icon='info-sign')).add_to(cluster)
folium.Marker(location = [-22.8425423,-47.2963221], popup = '30',icon = folium.Icon(color='blue', icon='info-sign')).add_to(cluster)
folium.Marker(location = [-9.9951627,-68.7029273], popup = '30',icon = folium.Icon(color='blue', icon='info-sign')).add_to(cluster3)
#folium.CircleMarker(location=[-23.8641866,-46.4303154], radius=25, popup='<b>SANTOS</b>', color='#3186cc', fill=True, fill_color='#3186cc').add_to(cluster)

#BOTÃO DE CONTROLE "ESTADOS"
folium.LayerControl().add_to(mapa)

#HTML: SALVAR ARQUIVO
mapa.save('mapa.html')