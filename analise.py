#%%
import os
import pandas as pd
import time
import seaborn as sns
from datetime import datetime
import matplotlib.pylab as plt

#%%
df = pd.read_csv("CONTENT_INTERACTION\\ViewingActivity.csv")
# %%
df.head()
df.drop("Attributes", axis=1)
#%% 
df['Duracao'] = pd.to_timedelta(df['Duration'])
df["Titulo"] = "abc"
i = 0
for x in df.iterrows():
    df["Titulo"][i] = df["Title"][i].split(":")[0]
    i = i+1
# %%
df2 = df[["Duracao","Titulo", "Profile Name"]] \
        .groupby(["Profile Name", "Titulo"]) \
        .sum()
df2

#%%
df2.groupby(["Profile Name", "Titulo"]) \
    .sum() \
    .sort_values(["Profile Name", "Duracao"],
                  ascending = False).head(30)

# %%
df3 = df.copy()
df3.head()
# %%
i = 0
df3["Data"] = df3["Start Time"]
df3['Dia da Semana'] = 'abc'
df3['Horas'] = 1.23
df3['Mes'] = 'abc'
for x in df3.iterrows():

    df3["Data"][i] = datetime.strptime(df3["Start Time"][i].split()[0],
                                       '%Y-%m-%d')

    df3['Mes'][i] =  (str(df3["Start Time"][i].split('-')[0]) + '.' \
                 + str(df3["Start Time"][i].split('-')[1]))

    df3["Dia da Semana"][i] = (df3["Data"][i].strftime('%w') \
                              + " - " + df3["Data"][i].strftime('%a'))

    df3['Horas'][i] = (df3['Duracao'][i].days*24 \
                     + df3['Duracao'][i].seconds/360)

    i = i+1

df3
# %%
df3_p = df3[["Profile Name", "Dia da Semana", "Duracao",'Horas']] \
    .groupby(["Profile Name", "Dia da Semana"]) \
    .sum()

# %%
sns.lineplot(data = df3_p, x = "Dia da Semana", y="Horas")

# %%
df3_p
# %%
df4 = df3[['Mes','Horas']].groupby('Mes').sum()
df4
# %%
sns.set(context = 'paper', font = 'monospace', rc={'figure.figsize':(8,5)})

sns.lineplot(data=df4, x = 'Mes', y = 'Horas')
# %%

