# pip install openpyxl ---> for reading excel files
#  rm *.pdf ---> CMD command to remove pdf files
from fpdf import FPDF
import pandas as pd

df = pd.read_excel('data.xlsx')

for index, row in df.iterrows():
    pdf_file = FPDF(orientation='P', unit='pt', format='A4')
    pdf_file.add_page()

    pdf_file.set_font(family='Times', style='B', size=24)
    pdf_file.cell(w=0, h=50, txt=row['name'].title(), align='C', ln=1)

    for col in df.columns[1:]:
        pdf_file.set_font(family='Times', style='B', size=14)
        pdf_file.cell(w=100, h=25, txt=f"{col.title()}:")

        pdf_file.set_font(family='Times', size=14)
        pdf_file.cell(w=100, h=25, txt=row[col].title(), ln=1)

    pdf_file.output(f'{row["name"]}.pdf')
