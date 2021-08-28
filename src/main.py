import PyPDF2
def convert(filename):
    pdfFileObject = open(filename, 'rb')
 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
 
    print(" No. Of Pages :", pdfReader.numPages)
 
    pageObject = pdfReader.getPage(0)
 
    print(pageObject.extractText())
 
    pdfFileObject.close()
 