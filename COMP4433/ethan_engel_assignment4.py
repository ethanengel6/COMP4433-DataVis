import pandas as pd
import json
from geopy.geocoders import ArcGIS
import folium
import matplotlib.pyplot as plt

sturm_df=pd.read_csv("https://raw.githubusercontent.com/SamanAl/Winter-Quarter-DU/master/Sample%20Data/SturmData_csv.txt?token=ASM5ERGHXQLRQGNPTMBKAXTAHIFKM")
sturm_df.loc[sturm_df['debtfree'] > 1920, 'debtfree'] = None
sturm_df.loc[sturm_df['effectivemwpa'] > 1920, 'effectivemwpa'] = None
sturm_df.loc[sturm_df['earnings'] > 1920, 'earnings'] = None
sturm_df.loc[sturm_df['wills'] > 1920, 'wills'] = None
sturm_df.loc[sturm_df['soletrader'] > 1920, 'soletrader'] = None


with open('us-states.json')  as json_data2:
    states_data2=json.load(json_data2)

for index in range(len(states_data2['features'])-1,-1,-1):
    if states_data2['features'][index]['id']== 'HI' or  states_data2['features'][index]['id']=='AK':
        del states_data2['features'][index]


debtfree_map = folium.Map(location=[40, -99], zoom_start=6)
folium.Choropleth(
    geo_data=states_data2,
    name="choropleth",
    data=sturm_df,
    columns=['state', 'debtfree'],
    nan_fill_color='black',
    nan_fill_opacity=1,
    key_on='feature.id',
    fill_color='YlGnBu',
    fill_opacity=.5,
    line_opacity=.2,
    legend_name='Passage Year',
    smooth_factor=0).add_to(debtfree_map)
folium.LayerControl().add_to(debtfree_map)
title_html = '''
             <h3 align="center" style="font-size:20px"><b>Year of passage of state law protecting married women’s separate property from her husband’s debts. (Black = no such law passed)</b></h3>
             '''
debtfree_map.get_root().html.add_child(folium.Element(title_html))
folium.LayerControl().add_to(debtfree_map)
debtfree_map.save('debtfree_map.html')

effectivemwpa_map = folium.Map(location=[40, -99], zoom_start=6)
folium.Choropleth(
    geo_data=states_data2,
    name="choropleth",
    data=sturm_df,
    columns=['state', 'effectivemwpa'],
    nan_fill_color='black',
    nan_fill_opacity=1,
    key_on='feature.id',
    fill_color='YlGnBu',
    fill_opacity=.5,
    line_opacity=.2,
    legend_name='Passage Year',
    smooth_factor=0).add_to(effectivemwpa_map)
folium.LayerControl().add_to(effectivemwpa_map)
title2_html = '''
             <h3 align="center" style="font-size:20px"><b>Year of passage of state law granting married women control and management rights over their separate property. (Black = no such law passed)</b></h3>
             '''
effectivemwpa_map.get_root().html.add_child(folium.Element(title2_html))
folium.LayerControl().add_to(effectivemwpa_map)
effectivemwpa_map.save('effectivemwpa_map.html')

earnings_map = folium.Map(location=[40, -99], zoom_start=6)
folium.Choropleth(
    geo_data=states_data2,
    name="choropleth",
    data=sturm_df,
    columns=['state', 'earnings'],
    nan_fill_color='black',
    nan_fill_opacity=1,
    key_on='feature.id',
    fill_color='YlGnBu',
    fill_opacity=.5,
    line_opacity=.2,
    legend_name='Passage Year',
    smooth_factor=0).add_to(earnings_map)
folium.LayerControl().add_to(earnings_map)
title3_html = '''
             <h3 align="center" style="font-size:20px"><b>Year of passage of state law granting married women ownership of their wages or earnings on par with other separate property (Black = no such law passed)</b></h3>
             '''
earnings_map.get_root().html.add_child(folium.Element(title3_html))
folium.LayerControl().add_to(earnings_map)
earnings_map.save('earnings_map.html')

wills_map = folium.Map(location=[40, -99], zoom_start=6)
folium.Choropleth(
    geo_data=states_data2,
    name="choropleth",
    data=sturm_df,
    columns=['state', 'wills'],
    nan_fill_color='black',
    nan_fill_opacity=1,
    key_on='feature.id',
    fill_color='YlGnBu',
    fill_opacity=.5,
    line_opacity=.2,
    legend_name='Passage Year',
    smooth_factor=0).add_to(wills_map)
folium.LayerControl().add_to(wills_map)
title4_html = '''
             <h3 align="center" style="font-size:20px"><b>Year of passage of state law granting married women the ability to write wills without their husband's consent or other restrictions (Black = no such law passed)</b></h3>
             '''
wills_map.get_root().html.add_child(folium.Element(title4_html))
folium.LayerControl().add_to(wills_map)
wills_map.save('wills_map.html')

soletrader_map = folium.Map(location=[40, -99], zoom_start=6)
folium.Choropleth(
    geo_data=states_data2,
    name="choropleth",
    data=sturm_df,
    columns=['state', 'soletrader'],
    nan_fill_color='black',
    nan_fill_opacity=1,
    key_on='feature.id',
    fill_color='YlGnBu',
    fill_opacity=.5,
    line_opacity=.2,
    legend_name='Passage Year',
    smooth_factor=0).add_to(soletrader_map)
folium.LayerControl().add_to(soletrader_map)
title5_html = '''
             <h3 align="center" style="font-size:20px"><b>Year of passage of state law granting married women as a class the right to sign contracts and engage in business without consent of husband (Black = no such law passed)</b></h3>
             '''
soletrader_map.get_root().html.add_child(folium.Element(title5_html))
folium.LayerControl().add_to(soletrader_map)
soletrader_map.save('soletrader_map.html')
