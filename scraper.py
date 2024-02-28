from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

table = soup.find_all('table')[1]

titles = table.find_all('th')

titles_list = [title.text.strip() for title in titles]

rows = table.find_all('tr')

df = pd.DataFrame(columns=titles_list)

for row in rows[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    
    length = len(df)
    df.loc[length] = individual_row_data

print(df)

df.to_csv('results.csv', index = False)
