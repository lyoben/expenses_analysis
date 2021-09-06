import pandas as pd
import numpy as np
import user_get as ug
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

print('Choose a month to find out the expenses for a particular month, categorized based on the type of expenses. Data available only between Sep 2020 and Feb 2021')
Year = ug.class_year.input_year()
Month = ug.class_month.input_month()
user_date = Month + ' ' + Year
Date = ug.class_date(user_date).date_format()
print('Expenses in', user_date)


read_file = pd.read_csv('main_2020.csv', usecols=['Year','Month','Type','Cost'], parse_dates=[['Month','Year']], low_memory=False)
user_file = read_file.loc[(read_file['Month_Year'] == Date) & read_file['Type'] & read_file['Cost']]
pivot_file = pd.pivot_table(user_file, values=['Cost'], index=['Type'], aggfunc=np.sum).reset_index()


try:
    plt.bar(pivot_file.Type, pivot_file.Cost)
    plt.title('Expenses in' + ' ' + user_date)
    plt.show()
except:
    AttributeError
    print('Selected month must be in between Sep 2020 and Feb 2021')


