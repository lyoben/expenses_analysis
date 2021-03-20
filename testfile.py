import pandas as pd
import matplotlib
import user_get as ug
import datetime
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('TkAgg')

#Create random 2 colums and export to CSV
'''
rnum = np.random.randint(1, high=20, size=20)
month = ['Jan', 'Feb', 'Mar']
rmonth = np.random.choice(month, 20)
list = [rmonth, rnum]
df = pd.DataFrame(list).transpose()
df.to_csv('test.csv', index=None, header=None, encoding='utf-8')
'''


#pivot table
'''
read_file = pd.read_csv('test.csv')
df = pd.pivot_table(read_file, values=['15'], index=['Feb'], aggfunc=np.sum)
'''

#plotting
'''
num = range(1,11)
list = [[i, i ** 2] for i in num]

df = pd.DataFrame(list, num, ['x','y'])
print(df.head())

plt.plot(df.x, df.y)
plt.title('Exponential')
plt.show()'''


df = pd.read_csv('testnew.csv')
print(df.head())

plt.bar(df.Type, df.Cost)
for index, value in enumerate(df.Cost):
    plt.text(value, index, str(df.Cost))
plt.show()


'''
plt.plot(df.Type, df.Cost)
plt.title('Exponential')
plt.show()'''