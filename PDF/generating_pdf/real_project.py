from fpdf import FPDF
import pandas as pd

df = pd.read_excel('real_project.xlsx')

for index, row in df.iterrows():
    pdf_file = FPDF(orientation='P', unit='pt', format='A4')
    pdf_file.add_page()

    pdf_file.set_font(family='Times', style='B', size=16)
    pdf_file.cell(w=0, h=50, txt=row['F.I.SH'].title(), align='C', ln=1)

    print(row['F.I.SH'])

    for col in df.columns[1:]:
        pdf_file.set_font(family='Times', style='B', size=14)
        pdf_file.cell(w=200, h=25, txt=f"{col.title()}:")

        pdf_file.set_font(family='Times', size=14)
        pdf_file.multi_cell(w=300, h=25, txt=str(row[col]))

    pdf_file.output(f'data/{row["F.I.SH"]}.pdf')
