# Program that scans PDF and DOCX files and finds most frequent words
# By: Matas Sabaliauskas
# Email: matas.sabal@gmail.com
# Note: preferred format is DOCX

#Note: Change CL1.docx and CL1.pdf to whatever document name you are using. Or change your documents to CL1 filename


FREQUENTWORDS = 10                   # Choose how many frequent words are required
from collections import Counter
import docx
import PyPDF2


#DOCX READER
def ReadingTextDocuments(filename):
    doc = docx.Document('CL1.docx')
    completedText = []

    for paragraph in doc.paragraphs:
        completedText.append(paragraph.text)

    return '\n' .join(completedText)

print(ReadingTextDocuments('CL1.docx'))




#PDF READER
def PDFReader(filename):
    pdfFile = "CL1.pdf"     #select the file here

    pdfRead = PyPDF2.PdfFileReader(pdfFile) #function is to read the first page of the file
    page = pdfRead.getPage(0)               #gets only 0th (first) page
    pageContent = page.extractText()        #extracts text into pageContent
    print(pageContent)                      #prints pageContent

    return pageContent


#MostFrequentWords

data_set_docx = ReadingTextDocuments('CL1.docx')
data_set_pdf = PDFReader('CL1.pdf')

# split() returns list of all the words in the string
split_it_docx = data_set_docx.split()
split_it_pdf = data_set_pdf.split()

# Pass the split_it list to instance of Counter class.
Counter_docx = Counter(split_it_docx)
Counter_pdf = Counter(split_it_pdf)


# most_common() produces k frequently encountered
# input values and their respective counts.
most_frequent_docx = Counter_docx.most_common(FREQUENTWORDS)
print("The most frequent keywords in DOCX were:")
print(most_frequent_docx)

most_frequent_pdf = Counter_pdf.most_common(FREQUENTWORDS)
print("The most frequent keywords in PDF were:")
print(most_frequent_pdf)

