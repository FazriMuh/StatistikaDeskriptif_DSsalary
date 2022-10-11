import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.set_printoptions(threshold=np.inf)

df = pd.read_csv('ds_salaries.csv')

x = df[['job_title', 'salary_in_usd','company_location']]
y = x.groupby('job_title').max()

print("\nGaji terbesar untuk setiap posisi-nya adalah\n")
print(y)

print("\nDan negara yang memiliki gaji terbesar untuk setiap posisi nya adalah\n")

z = y.groupby(["company_location"]).size().reset_index(name="Jumlah")
fig = plt.figure(figsize =(10, 7))

print(z)

plt.pie(z['Jumlah'], labels = z['company_location'],autopct='%1.2f%%')
plt.show()