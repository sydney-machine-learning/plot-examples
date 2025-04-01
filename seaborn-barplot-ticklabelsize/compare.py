
import matplotlib.pyplot as plt

import pandas as pd

import seaborn as sns

sns.set_theme()
sns.set_context("talk")
sns.set_theme(style="whitegrid")


aca = pd.read_csv('academics.csv')  

 

cols = ['green', 'blue', 'blue', 'red','green', 'purple','red', 'red', 'red','red', 'orange', 'black', 'red','brown', 'green','red','black']

print(aca)

# Draw a nested barplot by species and sex
g = sns.catplot(
    data=aca, kind="bar",
    x="Name", y="h-index",   palette=cols, alpha=.6, height=6
)
 

g.despine(left=True)

g.ax.set_xlabel("",fontsize=15)
g.ax.set_ylabel("h-index",fontsize=15) 
g.tick_params(axis='x', rotation=90)

g.tick_params(labelcolor='black', labelsize='medium', width=3)

plt.tight_layout()
plt.axhline(y=21, color='red') 

plt.axhline(y=32)
 
plt.savefig('compareaca.png')
plt.show()
