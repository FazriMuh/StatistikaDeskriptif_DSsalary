import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.set_printoptions(threshold=np.inf)

df = pd.read_csv('ds_salaries.csv')
x = df.loc[(df['company_location'] == 'US') & (df['job_title'].isin([ 'Principal Data Engineer',
                                                                     'Data Analytics Lead',
                                                                     'Data Engineer',
                                                                     'Data Scientist']))]

x1 = x[['job_title','salary_in_usd','company_location','company_size']]

z = x.loc[x['job_title'] == 'Principal Data Engineer']
z2 = z[['experience_level','employment_type','salary_in_usd', 'company_size']]
print(z2,'\n')

#Fakta = Posisi PDE hanya di miliki oleh negara US
x2 = df.loc[(df['job_title'] == 'Principal Data Engineer')]
z3 = x2[['experience_level','employment_type','salary_in_usd','company_location', 'company_size']]
print(z3,'\n')

result = x1.groupby('job_title').agg({'salary_in_usd': ['mean', 'min', 'max']})
print(result)

y = df[['job_title', 'salary_in_usd','company_location']]

print("\nDari Seluruh Dunia, Gaji tertinggi di miliki oleh : ")
print(y.loc[y['salary_in_usd'].idxmax()],"\n")



