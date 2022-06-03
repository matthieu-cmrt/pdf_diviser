from PyPDF2 import PdfFileWriter, PdfFileReader
import os

# for each pdf in src folder, path = src/file.pdf and name = file
for file in os.listdir("src"):
    # if file is a pdf
    if not file.endswith(".pdf"):
        continue
    path = "./src/" + file
    name = file[:-4]    
    inputpdf = PdfFileReader(open   (path, "rb"))

    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("./out/"+name+"-page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)