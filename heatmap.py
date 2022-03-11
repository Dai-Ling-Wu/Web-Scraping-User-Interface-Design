# -*- coding: utf-8 -*-

import pandas as pd
import json
SF_maps=json.load(open("Analysis Neighborhoods.geojson",'r'))
SF_nb=[]


for i in range(len(SF_maps['features'])):
    SF_nb.append(SF_maps['features'][i]['properties']['nhood'])
a=0
mapid={}
mapid_inv={}
for feature in SF_maps['features']:
    feature['id']=a
    mapid[feature['properties']['nhood']]= feature['id']
    mapid_inv[feature['id']]=feature['properties']['nhood']
    a+=1
    
    
df=pd.read_csv('data.csv')
data=df[["Incident Year","Incident ID","Incident Code","Incident Category","Incident Subcategory","Analysis Neighborhood","Latitude","Longitude"]]
data.dropna(inplace=True)
data.drop_duplicates('Incident ID',inplace=True)
incidentlist=data["Incident Category"].unique()
incidentlist.sort()
data['id']=data['Analysis Neighborhood'].apply(lambda x: mapid[x])
criteria=['Arson','Assault','Burglary','Disorderly Conduct', 'Drug Offence', 'Homicide',
          'Human Trafficking (A), Commercial Sex Acts','Human Trafficking (B), Involuntary Servitude',
          'Human Trafficking, Commercial Sex Acts', 'Larceny Theft','Malicious Mischief',
          'Motor Vehicle Theft','Motor Vehicle Theft?','Other Offenses','Prostitution', 'Rape',
          'Robbery', 'Sex Offense', 'Stolen Property','Suspicious', 'Suspicious Occ',
          'Vandalism','Weapons Carrying Etc','Weapons Offence', 'Weapons Offense']
r_data=data[data["Incident Category"].isin(criteria)]
r_data=r_data[data["Incident Year"]==2021]

a=r_data[['id','Incident ID']].groupby(['id'],as_index=False).count()
a['neighborhood']=a['id'].apply(lambda x: mapid_inv[x])
a.rename(columns={'Incident ID':'Number of Incidents'},inplace=True)

import plotly.express as px
import plotly.io as pio
pio.renderers.default='browser'
fig=px.choropleth(a,
                  locations='id',
                  geojson=SF_maps,
                  color='Number of Incidents',
                  hover_name='neighborhood',
                  color_continuous_scale=px.colors.sequential.OrRd)
fig.update_geos(fitbounds="locations",visible=False)
fig.show()
