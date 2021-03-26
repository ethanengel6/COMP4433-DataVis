import pandas as pd
import folium
from shapely.geometry import Polygon, LinearRing
import numpy as np
import json
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file,show

#Part1
lat_lon_df=pd.read_csv("capitals_lat_lon.csv",sep='\t')

coords_list=[]
for q in range(len(lat_lon_df)):
    coords_list.append([lat_lon_df.iloc[q]['Latitude'],lat_lon_df.iloc[q]['Longitude']])

cap_map=folium.Map(location=[0,0],zoom_start=6)
for coord in coords_list:
    cap_map.add_child(folium.Marker(location=coord,popup="World Capital City",icon=folium.Icon(color="blue")))

cap_map.save("cap_map.html")

#Part2
Nouakchott=[18.0735, -15.9582]
Asmara=[15.3229,38.9251]
Port_Elizabeth=[-33.9608, 25.6022]

Africa_triangle_map=folium.Map(location=[0,8],zoom_start=6)
Africa_triangle_map.add_child(folium.Marker(location=Nouakchott,popup="Nouakchott",icon=folium.Icon(color="blue")))
Africa_triangle_map.add_child(folium.Marker(location=Asmara,popup="Asmara",icon=folium.Icon(color="blue")))
Africa_triangle_map.add_child(folium.Marker(location=Port_Elizabeth,popup="Port Elizabeth",icon=folium.Icon(color="blue")))
Africa_triangle_map.save("Africa_triangle.html")

Africa_polygon=Polygon([(Nouakchott),(Asmara),(Port_Elizabeth)])
print(Africa_polygon.area,Africa_polygon.length)

#Part3

with open('kan_neb.json') as json_data4:
    kan_neb_dict=json.load(json_data4)

kan_list=kan_neb_dict['features'][0]['geometry']["coordinates"][0]
kan_tuples=[tuple(kan) for kan in kan_list]
neb_list=kan_neb_dict['features'][1]['geometry']["coordinates"][0]
neb_tuples=[tuple(neb) for neb in neb_list]

kan_ring = LinearRing(kan_tuples)
x, y = kan_ring.xy
neb_ring=LinearRing(neb_tuples)
x2,y2=neb_ring.xy
fig = plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
ax.plot(x,y,x2,y2)
ax.set_xlabel('longitude')
ax.set_ylabel('latitude')
ax.set_title('Kansas & Nebraska')
plt.show()

#Part4
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
rand_hap=np.random.rand(50)*6+2
hap_dict={'state':states,'happiness_index':rand_hap}
hap_df=pd.DataFrame(hap_dict)

with open('us-states.json')  as json_data3:
    states_data3=json.load(json_data3)

hap_map = folium.Map(location=[40, -99], zoom_start=6)
folium.Choropleth(
    geo_data=states_data3,
    name="choropleth",
    data=hap_df,
    columns=['state', 'happiness_index'],
    key_on='feature.id',
    fill_color='YlGnBu',
    fill_opacity=.5,
    line_opacity=.2,
    legend_name='2=Pure Misery 8=Ecstatic Elation',
    smooth_factor=0).add_to(hap_map)
folium.LayerControl().add_to(hap_map)
title_html = '''
             <h3 align="center" style="font-size:20px"><b>Happiness Index by state</b></h3>
             '''
hap_map.get_root().html.add_child(folium.Element(title_html))
folium.LayerControl().add_to(hap_map)
hap_map.save('hap_map.html')

#Part5
exp_values=np.random.exponential(50,500)
output_file('week5_hist.html')
xx,edges=np.histogram(exp_values,bins=20,range=[0,160])
hist_df=pd.DataFrame({'xx':xx,'left':edges[:-1],'right':edges[1:]})
p=figure(plot_width=1200,plot_height=500)
p.quad(bottom=0,top=hist_df['xx'],left=hist_df['left'],right=hist_df['right'],fill_color='blue',line_color='black')
show(p)
