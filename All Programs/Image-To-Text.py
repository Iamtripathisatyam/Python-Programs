import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd=r"C:\Users\Dell\AppData\Local\Tesseract-OCR\tesseract.exe"
img=Image.open("aj.jpg")
text=pytesseract.image_to_string(img)
print(text)
