# pip install PyMuPDF
# pip install tabula
# pip install tabula-py

import fitz
import tabula


def get_txt_method_one():
    with fitz.open('students.pdf') as pdf:
        for page in pdf:
            print(page.get_text())


def get_txt_method_two():
    with fitz.open('students.pdf') as pdf:
        text = ''
        for page in pdf:
            text += f"{20 * ('-')}\n"
            text += page.get_text()
        print(text)


def get_excel_file_data():
    table = tabula.read_pdf('weather.pdf', pages=1)
    # print(table[0])
    table[0].to_csv("output_weather.csv", index=None)


get_excel_file_data()
