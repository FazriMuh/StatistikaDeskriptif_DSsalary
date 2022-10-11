import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)

df = pd.read_csv('ds_salaries.csv')

x = df.loc[df['job_title'] == 'Data Scientist']
y = x[[ 'company_location', 'salary_in_usd']]

#menggunakan nilai maksimum
print("Posisi Data Scientist dengan gaji tertinggi, berasal dari sebuah perusahan yang terletak dari negara : ")

print(y.loc[y['salary_in_usd'].idxmax()],"\n")


#menggunakan rata-rata
mean = y.groupby('company_location', as_index=False).mean()
mean['salary_in_usd'] = mean['salary_in_usd'].astype(int)
mean.plot.bar('company_location', 'salary_in_usd')
plt.title("Rata-Rata")

print(mean)


print("\nJika menggunakan rata-rata, maka negara dengan gaji Data Scientist terbesar adalah :")
print(mean.loc[mean['salary_in_usd'].idxmax()])

plt.show()