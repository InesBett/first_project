import pandas as pd
import requests
import time
from dotenv import load_dotenv
import os 
import warnings
warnings.filterwarnings("ignore")

df_final= pd.read_csv("final_weather_API_df_bigger_done")

df_final

df_final.drop("Unnamed: 0", axis=1, inplace=True)

import seaborn as sns
import matplotlib.pyplot as plt 

top_10_countries= df_final[["incident", "country"]].value_counts().reset_index()
top_10_countries_1= top_10_countries.head(10)
top_10_countries_1

sns.barplot(x='incident', y='count', hue='country', data=top_10_countries_1)
plt.show()

df_x= df_final["incident"].value_counts().reset_index()
df_x

sns.barplot(x='incident', y='count',data= df_x)
plt.title('Top Incidents')
plt.xlabel('Incidents')
plt.ylabel('Number of Incidents')
plt.show()

import plotly.express as px

fig = px.choropleth(df_final, locations='country', 
                    locationmode='country names',
                    color='incident', 
                    color_continuous_scale='Reds', 
                    title='Top Incidents by Country')
fig.show()

flood_count = df_final[["incident","country"]].value_counts().reset_index()
top_flood = flood_count.head(10)
top_flood

sns.barplot(x='incident', y='count', hue= "country",data= top_flood)
plt.title('Top 10 countries by Forest Fires')
plt.xlabel('Incidents')
plt.ylabel('Forest Fires')
plt.legend(title='Top 10 countries')
plt.show()

df_fires= df_final[["incident", "country"]].value_counts().reset_index()
df_fires= df_fires.head(10)
df_fires

fig = px.choropleth(df_fires, locations='country', 
                    locationmode='country names',
                    color='incident', 
                    color_continuous_scale='Reds', 
                    title='Top 10 Forest Fires by Country')
fig.show()



