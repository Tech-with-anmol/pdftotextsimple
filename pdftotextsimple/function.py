import PyPDF2
def convert(filename):
    try:  
        pdfFileObject = open(filename, 'rb')
    except Exception as e:
        print("you have done something wrong means wrong file name or directory")
        print("this is problem" + e)
 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
 
    print(" No. Of Pages :", pdfReader.numPages)
 
    pageObject = pdfReader.getPage(0)
 
    print(pageObject.extractText())
 
    pdfFileObject.close()
 