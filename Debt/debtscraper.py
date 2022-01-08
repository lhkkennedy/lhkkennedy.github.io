import pandas as pd
import requests
import os
from bs4 import BeautifulSoup

#downloading the source code for the URL then searching for a table
URL = "https://tradingeconomics.com/country-list/government-debt-to-gdp"
html = requests.get(URL)
soup = BeautifulSoup(html.content, 'html.parser')
table = soup.find_all("table", class_="table table-hover table-heatmap")
#searching through the tables source code to find the rows.
table_rows = table[0].find_all('tr')

df = pd.DataFrame()
# I iterate through the array of rows and extract the country names and values
# Countries with multiple words required special treatment 
# They would take up multiple places in the row array shifting the value place
for tr in table_rows:
    s = table_rows.index(tr)
    items = tr.text
    # Split the text elements in each row text into an array
    arr = items.split()
    extra = len(arr) - 5
    country = arr[0]
    value = arr[1+extra]
    # If the coutntry name is longer than one word we loop until all words are joined.
    for x in range(extra):
        country = country + ' ' + arr[x+1]
    results = [country, value]
    print(results)
    # The data is placed into a data frame to be formated
    df_t = pd.DataFrame(results)
    df_t.columns = ['Data']
    df[s] = df_t['Data']

# Transpose and remove the first row.
df = df.T
df = df.iloc[1: , :]
df.columns = ['Country', 'Debt-to-GDP']
print(df)

#save to csv
filename = 'Debt-to-GDP.csv'
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
filelocation = os.getcwd()
print("Saving as:  [ " + filename + " ]  in:  [ " + filelocation + " ] ")
df.to_csv(filename)
