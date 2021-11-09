import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')

def color_changer(elev):
    if(elev < 1000):
        return 'green'
    elif(1000 <= elev < 3000):
        return 'orange'
    else:
        return 'red'

latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start = 6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

fgv = folium.FeatureGroup(name = "Volcanoes")

for lat, lon,elev in zip(latitude,longitude, elevation) :
    fgv.add_child(folium.CircleMarker(location=[lat,lon], radius=6, popup=elev, fill_color=color_changer(elev), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name = "population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function= lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 100000000 else 'orange' if 100000000 <= x['properties']['POP2005'] < 200000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")



