import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)

df = pd.read_csv('ds_salaries.csv')
x = df.loc[df['company_location'] == 'US']
y = x[['job_title', 'salary_in_usd']]

#menggunakan nilai maksimum
print("Posisi dengan gaji tertinggi dari negara US Adalah : ")

print(y.loc[y['salary_in_usd'].idxmax()])

#menggunakan rata-rata
mean = y.groupby('job_title', as_index=False).mean()
print(mean)
mean.plot.bar('job_title', 'salary_in_usd')
plt.title("Rata-Rata")

print("\njika menggunakan rata-rata, maka posisi dengan gaji terbesar adalah :")
print(mean.loc[mean['salary_in_usd'].idxmax()])

plt.show()
