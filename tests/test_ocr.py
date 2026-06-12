import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

img = Image.open(r"C:\Invoice-Intelligence-AI\invoices\invoice.jpeg")

text = pytesseract.image_to_string(img)

print(text[:1000])