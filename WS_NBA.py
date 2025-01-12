import pandas as pd
import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.basketball-reference.com/leagues/NBA_2018_totals.html')

if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content

#   Criando objeto e acessando elementos chamando o método find.
soup = BeautifulSoup(content,'html.parser')
table = soup.find(name='table')

table_str = str(table)
df = pd.read_html(table_str)

# Loop com range para iterar estatísticas de 2013 a 2018

def scrape_stats(base_url, year_start, year_end):
    years = range(year_start,year_end+1,1)

    final_df = pd.DataFrame()

    for year in years:
        print('Extraindo ano {}'.format(year))
        req_url = base_url.format(year)
        req = requests.get(req_url)
        soup = BeautifulSoup(req.content, 'html.parser')
        table = soup.find('table', {'id':'totals_stats'})
        df = pd.read_html(str(table))[0]
        df['Year'] = year

        final_df = final_df.append(df)

        return final_df

    url = 'https://www.basketball-reference.com/leagues/NBA_{}_totals.html'

    df = scrape_stats(url, 2013,2018)
























