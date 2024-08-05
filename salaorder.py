# importaing libraries & data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Sales_Order=pd.read_csv("Order_details.csv")

# Sales_Order.head()
print(Sales_Order.head())

# Convert Data Time and add new column from transcation

Sales_Order['Time']= pd.to_datetime(Sales_Order['Transaction Date'])

# Extract hour from Transcation date column

Sales_Order['Hour'] = (Sales_Order['Time']).dt.hour

print(Sales_Order.head())

#Calculate and fine “n” busiest hours

#n -24 in this case can be modified to find top n busiest hours

timebusiest1=Sales_Order['Hour'].value_counts().index.tolist()[:24]

timebusiest2=Sales_Order['Hour'].value_counts().index.tolist()[:24]

#Stack indiciec hours and frequencies together to yield final result

timeBusy=np.column_stack((timebusiest1,timebusiest2))
print("Hours of the Day" +"\t" + "Cumulative No. of purchase \n")
print('\n'.join('\t\t'.join(map(str,row)) for row in timeBusy))

#Customize the data for visualization 
timeBusy= Sales_Order['Hour'].value_counts()
timebusiest1=[]

for i in range(0,23):
    timebusiest1.append(i)

timebusiest2=timeBusy.sort_index()
timebusiest2.tolist()
timebusiest2= pd.DataFrame(timebusiest2)

# Data Visualizaton with Matplotlib

plt.figure(figsize=(20, 10)) 
  
plt.title('Sales per Hour (overall week trend)', fontdict={'fontname': 'monospace', 'fontsize': 30}, y=1.05) 
plt.ylabel("Total Purchases ", fontsize=18, labelpad=20) 
plt.xlabel("Hour", fontsize=18, labelpad=20) 
plt.plot(timebusiest1, timebusiest2, color='m') 
plt.grid() 
plt.show() 

# data visulization with boxplot

plt.figure(figsize=(6,6))
sns.boxplot(x=timebusiest1, y='Hour', data=timebusiest2)


# Data Visualization with Scatter plot

plt.figure(figsize=(20, 10))

plt.title('Sales per Hour (overall week trend)', fontdict={'fontname': 'monospace', 'fontsize': 30}, y=1.05)
plt.ylabel("Total Purchases", fontsize=18, labelpad=20)
plt.xlabel("Hour", fontsize=18, labelpad=20)
plt.scatter(timebusiest1, timebusiest2, color='m')
plt.grid()
plt.show()

