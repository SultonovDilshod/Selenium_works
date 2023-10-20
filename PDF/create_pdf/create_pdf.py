from fpdf import FPDF

pdf_file = FPDF(orientation='P', unit='pt', format='A4')
pdf_file.add_page()

pdf_file.image('image_heroes.png', w=0, h=180, x=180)

pdf_file.set_font(family='Times', style='B', size=24)
pdf_file.cell(w=0, h=50, txt='My super heroes', align='C', ln=1)

pdf_file.set_font(family='Times', style='B', size=14)
pdf_file.cell(w=0, h=25, txt='About heroes', ln=1)

pdf_file.set_font(family='Times', size=12)
text = 'Every person has their own idol, somehow their idol can be considered as their superhero because of several ' \
       'reasons. According to Rosenberg (2010), superhero means someone who commits only a single heroic act while ' \
       'exhibiting more than normal talents or abilities would not be classified as a superhero(p. 1). As stated by' \
       ' Rosenberg, that people who has exceptional talents can be considered as superhero. So, superhero is not ' \
       'just a fiction character from comic or anime but it also can be a real person.'
pdf_file.multi_cell(w=0, h=15, txt=text)

pdf_file.set_font(family='Times', style='B', size=14)
pdf_file.cell(w=100, h=25, txt='Kingdom:')

pdf_file.set_font(family='Times', size=14)
pdf_file.cell(w=100, h=25, txt='America', ln=1)

pdf_file.set_font(family='Times', style='B', size=14)
pdf_file.cell(w=100, h=25, txt='Reaching:')

pdf_file.set_font(family='Times', size=14)
pdf_file.cell(w=100, h=25, txt='Protect', ln=1)

pdf_file.output('result.pdf')
