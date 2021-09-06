import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat1 = list(data['LAT'])
lon1 = list(data['LON'])
elev1 = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6,tiles = 'Stamen Terrain')

fgv = folium.FeatureGroup(name = 'Volcanoes')

for lt, ln, el in zip(lat1, lon1, elev1):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(el)+"\nelev in m", parse_html = True), icon=folium.Icon(color=color_producer(el))))

fgp = folium.FeatureGroup(name = 'Population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 1000000 
else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save('Map1.html')

#lookup how to write a guide for the red yellow and orange colors
#for population