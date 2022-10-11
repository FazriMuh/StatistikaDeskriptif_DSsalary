import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)

df = pd.read_csv('ds_salaries.csv')
# x = df.loc[df['company_location'] == 'US']

y = df.pivot_table(columns=['job_title'], aggfunc='size') #Tabel Baru
rows = len(y.axes[0])
print("jumlah title job pada data adalah ",rows)

z = df.groupby(["job_title"]).size().reset_index(name="Jumlah")

print(z)
# print("\nJumlah total Posisi di negara US adalah ",rows,"\n")

print("\nPosisi yang paling banyak di pekerjakan di seluruh negara adalah")
print(z.loc[z['Jumlah'].idxmax()],"\n")

x = z[['job_title', 'Jumlah']]

plt.bar(x['job_title'],x['Jumlah'])
plt.xticks(rotation=90)

plt.show()
