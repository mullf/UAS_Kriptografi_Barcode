import barcode
from barcode.writer import ImageWriter
from PIL import Image

nm = ""
gambar = "https://mullf.github.io/"

ean = barcode.get('code128', gambar, writer=ImageWriter())
nama = input("Masukkan nama barcode")
ean.save(nama)
ean = Image.open(nama + ".png")
ean.show()
