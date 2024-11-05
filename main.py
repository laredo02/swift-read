

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4

def hello(c):
    c.drawString(100, 100, "Miguel Laredo")

c = canvas.Canvas("hello.pdf", pagesize=letter)

hello(c)
c.showPage()
c.save()


