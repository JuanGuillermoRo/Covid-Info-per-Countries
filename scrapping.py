#%%

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd 

#generar el dataframe
df = pd.read_csv("https://covid19.who.int/WHO-COVID-19-global-table-data.csv")

df = df.drop(['WHO Region', 'Cases - cumulative total per 100000 population',
              'Cases - newly reported in last 7 days per 100000 population',
              'Deaths - cumulative total per 100000 population',
              'Deaths - newly reported in last 7 days','Deaths - newly reported in last 7 days per 100000 population',
              'Transmission Classification'], axis=1)

df = df.set_index('Name')

#que va hacer el dataframe

df['Recovered']=df['Cases - cumulative total']-df['Deaths - cumulative total']

df = df.drop(['Cases - cumulative total', 'Deaths - newly reported in last 24 hours'], axis = 1)

inp = input("Enter Country: ")
df.loc[[inp]]

import matplotlib.pyplot as plt

recovered = df.at[inp, 'Recovered']
Deaths = df.at[inp,'Deaths - cumulative total']
new_Cases24 = df.at[inp, 'Cases - newly reported in last 24 hours'] 
new_Cases7 = df.at[inp, 'Cases - newly reported in last 7 days']
f = plt.figure(figsize=(6,8))
font = {
    'family': 'normal',
    'weight':'bold',
    'size':12
}

plt.rc('font',**font)
plt.rcParams.update({'text.color':"black",'axes.labelcolor':"black"})
plt.pie([recovered, Deaths,new_Cases24,new_Cases7], 
         labels=['Recovered','Deaths','New Cases /24hr','New Cases /7days'], 
         colors = ['lightgreen','red','pink','orange'], 
         explode=(0.0,0.3,0.2,0.1), startangle = 180, autopct = '%1.1f%%')

#displaying the plot

plt.title(inp)
plt.legend()
plt.show()


# %%
