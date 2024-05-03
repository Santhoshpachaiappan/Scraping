from bs4 import BeautifulSoup
import requests
url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
path=requests.get(url)
soup=BeautifulSoup(path.text,'html')
print(soup)

#getting the first table value
table=soup.find_all('table')[1]
print(table)

#Getting the table header 
world_titles=table.find_all('th')
world_table_titles=[title.text.strip() for title in world_titles]
print(world_table_titles)

#importing pandas liberary and forming a dataframe
import pandas as pd
df=pd.DataFrame(columns =world_table_titles)
df

#Acessings the each row of the table
Column_data=table.find_all('tr')[1:]
for row in Column_data:
    row_data=row.find_all('td')
    Individual_row_data=[data.text.strip() for data in row_data]

    length=len(df)
    df.loc[length]=Individual_row_data
df
df.to_csv(r'D:/Data/Companies.csv',index=False)
