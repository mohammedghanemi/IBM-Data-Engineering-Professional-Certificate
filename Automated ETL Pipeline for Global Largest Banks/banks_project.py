
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

def log_progress(message, log_file="code_log.txt"):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"{time_stamp} : {message}\n")
log_progress("Preliminaries complete. Initiating ETL process")
print("Log entry created in code_log.txt")

def extract(url="https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks",
            table_attribs={"class": "wikitable"}):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    table = soup.find("table", table_attribs)
    headers = [th.text.strip() for th in table.find_all("th")]
    rows = []
    for tr in table.find_all("tr")[1:]:
        cols = tr.find_all(["td", "th"])
        cols_text = [td.text.strip().replace('\n','') for td in cols]
        if cols_text:
            rows.append(cols_text)
    
    df = pd.DataFrame(rows, columns=headers)
    df = df[['Bank name', 'Market cap(US$ billion)']]
    df.rename(columns={'Bank name':'Name', 'Market cap(US$ billion)':'MC_USD_Billion'}, inplace=True)
    df['MC_USD_Billion'] = df['MC_USD_Billion'].str.replace(',','').astype(float)
    log_progress("Data extraction complete. Initiating Transformation process")
    return df

def transform(df, csv_path):
    exchange_rate_df = pd.read_csv(csv_path)
    exchange_rate = exchange_rate_df.set_index('Currency')['Rate'].to_dict()
    df['MC_GBP_Billion'] = [np.round(x * exchange_rate['GBP'], 2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x * exchange_rate['EUR'], 2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x * exchange_rate['INR'], 2) for x in df['MC_USD_Billion']]
    
    log_progress("Data transformation complete. Initiating Loading process")
    return df


def load_to_csv(df, output_path):
    df.to_csv(output_path, index=False)
    log_progress("Data saved to CSV file")
    
def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
    log_progress("Data loaded to Database as a table, Executing queries")
def run_query(query_statement, sql_connection):
    print(f"Query: {query_statement}")
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)
    print("\n" + "="*50 + "\n")
    return query_output

df_banks = extract(url="https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks",
                   table_attribs={"class": "wikitable"})

df_banks = transform(df_banks, 'exchange_rate.csv')

load_to_csv(df_banks, 'Largest_banks.csv')
conn = sqlite3.connect('Banks.db')
load_to_db(df_banks, conn, 'Largest_banks')
run_query("SELECT * FROM Largest_banks", conn)
run_query("SELECT AVG(MC_GBP_Billion) FROM Largest_banks", conn)
run_query("SELECT Name FROM Largest_banks LIMIT 5", conn)
conn.close()
log_progress("Process Complete")
print(f"\nMC_EUR_Billion[4]: {df_banks['MC_EUR_Billion'][4]}")