import PyPDF2

keyfile = open('US_Declaration.pdf', mode='rb')

pdf_reader = PyPDF2.PdfReader(keyfile)

print(len(pdf_reader.pages))

page_one = pdf_reader.pages[0]


print(page_one.extract_text() ) #adding a space allows the text to be more readable

keyfile.close()

f = open('US_Declaration.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(f)

first_page = pdf_reader.pages[0]

pdf_writer = PyPDF2.PdfWriter()

pdf_writer.add_page(first_page)

pdf_output = open('MY_BRAND_NEW.pdf','wb')

pdf_writer.write(pdf_output)

pdf_output.close()

f.close()

brand_new = open('MY_BRAND_NEW.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(brand_new)

print(len(pdf_reader.pages))

f = open('US_Declaration.pdf', 'rb')

pdf_text = [0]

pdf_reader = PyPDF2.PdfReader(f)

for p in range(len(pdf_reader.pages)):

    page = pdf_reader.pages[p]

    pdf_text.append(page.extract_text())

f.close()

print(pdf_text)

for page in pdf_text:
    print(page)
    print('\n')
    print('\n')
    print('\n')
    print('\n')