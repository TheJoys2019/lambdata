'''
Date Splitting Helper Function - Takes the date, divides it into individual columns and makes them numerical.

Ex: Date must be in string fromat (MM-DD-YYYY)
'''

def splitting_date(df):
  import datetime

  # Apply Date to Column
  def to_datetime(x):
    return datetime.datetime.strptime(x, '%b %d %Y')

  #Generate new column with function
  df['datetime'] = df['date'].apply(to_datetime)

  #Modify column to str
  df['datetime'] = df['datetime'].astype(str)

  #Split date column with sep
  df['date_sep'] = df['datetime'].str.split('-')

  #Feature engineering with split dates 
  df['year'] = pd.to_numeric(df['date_sep'].str[0])
  df['month'] = pd.to_numeric(df['date_sep'].str[1])
  df['day_of_month'] = pd.to_numeric(df['date_sep'].str[2])

  #Remove Sep Column
  df = df.drop(columns='date_sep')

  return df