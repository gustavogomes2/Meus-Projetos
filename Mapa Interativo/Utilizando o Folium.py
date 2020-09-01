import folium

mapa = folium.Map(
    location = [-13.7048968, -69.6590157],
    tiles = 'OpenStreetMap',
    zoom_start = 4)

folium.Marker(location = [-15.7750837,-48.0772776], popup = '<i>30 - BRASÍLIA</i>',icon = folium.Icon(color='blue', icon='info-sign')).add_to(mapa) 

for index, linha in 
folium.Marker(location = [-23.1119265,-47.2646612], popup = '<i>15 - INDAIATUBA-SP</i>',icon = folium.Icon(color='blue', icon='info-sign')).add_to(mapa)
folium.Marker(location = [-2.5606303,-44.3281622], popup = '<i>40 - SÂO LUIZ-MA</i>',icon = folium.Icon(color='blue', icon='info-sign')).add_to(mapa)
folium.Marker(location = [-22.7146204,-47.6918722], popup = '<i>3 - PIRACICABA-SP</i>',icon = folium.Icon(color='blue', icon='info-sign')).add_to(mapa)
folium.Marker(location = [-22.8425423,-47.2963221], popup = '<i>30 - SUMARÉ-SP</i>',icon = folium.Icon(color='blue', icon='info-sign')).add_to(mapa)
folium.Marker(location = [-9.9951627,-68.7029273], popup = '<i>30 - RIO BRANCO-ACRE</i>',icon = folium.Icon(color='blue', icon='info-sign')).add_to(mapa)

mapa.save('mapa.html')