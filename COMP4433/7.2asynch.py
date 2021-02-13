
from shapely.geometry import Polygon
pent1=Polygon([(-1,-1),(10,3),(20,4),(21,20),(7,10)])
print(pent1.area,pent1.length)


"""import folium
map=folium.Map(location=[50,-110],zoom_start=6)
map.add_child(folium.Marker(location=[13.4125,103.8670],popup="Angkor Wat Bruh",icon=folium.Icon(color='blue')))
map.add_child(folium.Marker(location=[41.583112,-93.741026],popup="Grandma's house",icon=folium.Icon(color='red')))

map.save("two_places.html")"""
