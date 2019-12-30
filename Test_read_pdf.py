import PyPDF2
pdfFileObject = open('SendRequest.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
DocInfo = pdfReader.getDocumentInfo()
print('Создан ' + DocInfo['/Creator'])
print('Изменён ' + str(DocInfo['/ModDate'])[2:10])
count = pdfReader.numPages

for i in range(count):
    print(i)
    page = pdfReader.getPage(i)
    print(page)
    print(page['/text'])
    print(page.extractText())

