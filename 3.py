import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)

df = pd.read_csv('ds_salaries.csv')
x = df.loc[df['company_location'] == 'US']

y = x.pivot_table(columns=['job_title'], aggfunc='size') #Tabel Baru

rows = len(y.axes[0])

print("\nJumlah total Posisi di negara US adalah ",rows,"\n")

z = x.groupby(["job_title"]).size().reset_index(name="Jumlah")

print(z)

print("\nPosisi yang paling banyak di pekerjakan di negara US adalah \n")
print(z.loc[z['Jumlah'].idxmax()],"\n")


y.plot.bar()
plt.xticks(rotation=90)

plt.show()
