import PyPDF2
import speaker


def readpage(pdfname):
  pdfFileObj = open(pdfname, 'rb')
  pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  pdfsize = pdfReader.numPages)
  for p in range(pdfsize-1):
    pageObj=pdfReader.getPage(p)
    speaker.speak(pageObj.extractText()))
  pdfFileObj.close()
