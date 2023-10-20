from fpdf import FPDF
import pandas as pd

# df_20 = pd.read_excel('data/2020_oylar.xlsx')
# df_21 = pd.read_excel('data/2021_oylar.xlsx')
# df_22 = pd.read_excel('data/2022_oylar.xlsx')

# ali = df_20.to_csv('2020.csv')
# print(ali)


df_20 = pd.read_csv('data/2020.csv')

for index, row in df_20.iterrows():
    print(row.head())
