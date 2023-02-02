import pandas as pd
# 1- load the file to pandas
data = pd.read_csv(r"C:\Users\pc\Downloads\temperature.csv",',')
# 2- display file info and print a list of all columns of data
print(data)
print()
print('list of all columns of data : ',list(data.columns))
# 3- select a city (any city from the data) and select one year
#(any one year from the data) and create a new datagram containing only the filters information
df1 = data[data['City'] == 'Paris']
df2 = df1[df1['year'] == 2003]
print(df2)
# 4- print the total number of records in the new data and the average temprecher
shape = df2.shape[0]
sum_temp = df2['AverageTemperatureFahr'].sum()
average_temprecher = sum_temp/shape
print(f'the total number of records in the new data : {shape}')
print(f'the average temprecher : {average_temprecher}')
