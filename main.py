from pypdf import PdfReader

reader = PdfReader("230703-g.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)
