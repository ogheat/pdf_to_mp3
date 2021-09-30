import pdfplumber
from gtts import gTTS

print("It is PDF to MP3 converter")
name = input("Print name of your pdf-file(without .pdf) ")
lang = input("Print language of the book in the IETF format(ex. 'ru' for russian, 'en' for english ")
print("Loading...If the file is large, it may take some time (up to 15 minutes)")
all_text = ""
pdf = pdfplumber.open(f'{name}.pdf')
for i in range(0,(len(pdf.pages))):
    page = pdf.pages[i]
    text = page.extract_text()
    if type(text) == str:
        all_text += text
pdf.close()
tts = gTTS(all_text,lang=f"{lang}")
tts.save('result/result.mp3')
print("File result.mp3 successful saved to the result folder ")














