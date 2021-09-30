import PyPDF2
from gtts import gTTS



print("It is PDF to MP3 converter")
name = input("Print name of your pdf-file(without .pdf) ")


all_text = ""
pdffileobj = open(f'{name}.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(pdffileobj)
x = pdfreader.numPages
for i in range(x):

    pageobj = pdfreader.getPage(i)
    text = pageobj.extractText()
    all_text += text


tts = gTTS(all_text)
tts.save('results/result.mp3')
print("File result.mp3 successful saved to the results folder ")














