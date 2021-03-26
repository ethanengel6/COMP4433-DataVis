import pandas as pd
import folium
import json
import matplotlib.pyplot as plt
import seaborn as sns

sl_trc_df=pd.read_csv("SL-TRC-data.csv",sep='\t')
district_counts = sl_trc_df['locad'].value_counts().to_dict()
counts_df=pd.DataFrame({'district' : district_counts.keys() , 'violations' : district_counts.values() })
id_dict={"kai":"1","ken":"2","kon":"3","bom":"4","kam":"5","koi":"6","por":"7","ton":"8","box":"9","bon":"10","moy":"11","puj":'12',"fre":"13"}
id_df=pd.DataFrame({'district':id_dict.keys(),'ID':id_dict.values()})
pop_dict={"kai":358190,"ken":497948,"kon":335401,"bom":408390,"kam":270462,"koi":265758,"por":453746,"ton":347197,"box":463668,"bon":139687,"moy":260910,"puj":228392,"fre":947122}
pop_df=pd.DataFrame({'district':pop_dict.keys(),'ID':pop_dict.values()})
df_merged1 = pd.merge(counts_df, id_df, on='district')
df_merged2 = pd.merge(df_merged1, pop_df, on='district')
df_merged2['ratio']=df_merged2['violations']/df_merged2['ID_y']*100000


with open('SLE_adm2_simp_001.json')  as sl_json_data:
    sl_json_data2=json.load(sl_json_data)

sl_map = folium.Map(location=[8,-13], zoom_start=7)
folium.Choropleth(
    geo_data=sl_json_data2,
    name="choropleth",
    data=df_merged2,
    columns=['ID_x', 'violations'],
    threshold_scale=[1200, 1600, 2000, 2400, 2800, 3200,3600],
    key_on='feature.properties.ID_2',
    fill_color='YlOrRd',
    fill_opacity=1,
    line_opacity=.2,
    smooth_factor=0).add_to(sl_map)
title_html = '''
             <h3 align="center" style="font-size:20px"><b>Total Crimes by District.  (Freetown & the surrounding western rural areas have been combined.)</b></h3>
             '''
sl_map.get_root().html.add_child(folium.Element(title_html))
folium.LayerControl().add_to(sl_map)
sl_map.save('sl_map.html')

sl_map2 = folium.Map(location=[8,-13], zoom_start=7)
folium.Choropleth(
    geo_data=sl_json_data2,
    name="choropleth",
    data=df_merged2,
    columns=['ID_x', 'ratio'],
    threshold_scale=[100, 400, 700,1000,1300,1600,1900],
    key_on='feature.properties.ID_2',
    fill_color='YlOrRd',
    fill_opacity=1,
    line_opacity=.2,
    smooth_factor=0).add_to(sl_map2)
title2_html = '''
             <h3 align="center" style="font-size:20px"><b>Total Crimes per 100,000 citizens by district.  (Freetown & the surrounding western rural areas have been combined.)</b></h3>
             '''
sl_map2.get_root().html.add_child(folium.Element(title2_html))
folium.LayerControl().add_to(sl_map2)
sl_map2.save('sl_map2.html')

plt.style.use('dark_background')
year_counts = sl_trc_df['n_yr'].value_counts().to_dict()
year_counts_df=pd.DataFrame({'year' : year_counts.keys() , 'Total Crimes of the Conflict' : year_counts.values() })
year_counts_df.sort_values(by=['year'],inplace=True)
year_plot = year_counts_df.plot.line(x='year', y='Total Crimes of the Conflict')
plt.show()

gend_hist_df=sl_trc_df.loc[(sl_trc_df['gendc'] != '?')]
hist_grid=sns.FacetGrid(gend_hist_df,col='gendc')
hist_grid=hist_grid.map(plt.hist,'age')
plt.suptitle('Age Distribution of Crime Victims (M/F) ', fontsize=18)
plt.tight_layout()
plt.show()

box_plots = sns.boxplot(x="age", y="violt", data=sl_trc_df)
plt.title('Age Distribution of Victims of Different Crimes', fontsize=18)
plt.tight_layout()
plt.show()

crime_counts = sl_trc_df['violt'].value_counts().to_dict()
keys = crime_counts.keys()
values = crime_counts.values()
plt.bar(keys, values)
plt.xticks(range(len(keys)),keys,rotation=30)
plt.title('Total Reported Counts of Different Crimes', fontsize=18)
plt.tight_layout()
plt.show()

ruf_df=sl_trc_df.loc[(sl_trc_df['p3_ruf'] == 't')]
ruf_crime_counts = ruf_df['violt'].value_counts().to_dict()
ruf_keys = ruf_crime_counts.keys()
ruf_values = ruf_crime_counts.values()

sla_df=sl_trc_df.loc[(sl_trc_df['p3_sla'] == 't')]
sla_crime_counts = sla_df['violt'].value_counts().to_dict()
sla_keys = sla_crime_counts.keys()
sla_values = sla_crime_counts.values()

afrc_df=sl_trc_df.loc[(sl_trc_df['p3_afrc'] == 't')]
afrc_crime_counts = afrc_df['violt'].value_counts().to_dict()
afrc_keys = afrc_crime_counts.keys()
afrc_values =afrc_crime_counts.values()

police_df=sl_trc_df.loc[(sl_trc_df['p3_police'] == 't')]
police_crime_counts = police_df['violt'].value_counts().to_dict()
police_keys = police_crime_counts.keys()
police_values =police_crime_counts.values()

def my_autopct(pct):
    return ('%.1f' % pct) if pct > 2 else ''
fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(14,6))
axes[0,0].pie(ruf_values,autopct=my_autopct,pctdistance=1.05)
axes[0,0].set_title('RUF - Revolutionary United Front')
axes[0,1].pie(sla_values,autopct=my_autopct,pctdistance=1.05)
axes[0,1].set_title('Sierra Leone Army')
axes[1,0].pie(afrc_values,autopct=my_autopct,pctdistance=1.05)
axes[1,0].set_title('Armed Forces Revolutionary Council')
axes[1,1].pie(police_values,autopct=my_autopct,pctdistance=1.05)
axes[1,1].set_title('Police officers including SSD division')
fig.legend(ruf_keys, loc='center')
fig.suptitle('Crimes(% of total) within Perpetrator Groups ', fontsize=16)
plt.show()
