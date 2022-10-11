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
y = x[['job_title', 'salary_in_usd']]

print(y)
y.boxplot(by ='job_title', column =['salary_in_usd'], grid = False)


#plt.xticks(rotation=45)
plt.rcParams["figure.figsize"] = [10.50, 7.50]
plt.rcParams["figure.autolayout"] = True

plt.show()


