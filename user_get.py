import datetime
import pandas as pd

#user input year
class class_year:
    def input_year():
        while True:
            try:
                user_year = str(input('Year: '))
                return user_year
                break
            except:
                print('Please input valid year')

#user input month
class class_month:
    def input_month():
        while True:
            try:
                list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                print('Choose a month from list')
                for i in list:
                    print(i, end=',')

                user_month = input('\nMonth: ')

                if user_month not in list:
                    print('wrong month')
                else:
                    return user_month
            except:
                continue

#format user input year/month into date format
class class_date:
    def __init__(self, date):
        self.date = date

    def date_format(self):
        self.date = datetime.datetime.strptime(self.date, '%b %Y').date()
        self.date = pd.Timestamp(self.date, hour=None, minute=None, second=None)
        return self.date