"""

Null Doctor Helper Function - A helper function responsible for filling the null values with the average or mean of that column

"""

def null_doctor(dataframe):
    dataframe = dataframe.fillna(dataframe.mean())
    return dataframe
