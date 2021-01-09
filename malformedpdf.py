import pdfrw
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() #Only the windows file box will appearing
uploaded_file = askopenfilename()#Input file

x = pdfrw.PdfReader(uploaded_file)
y = pdfrw.PdfWriter()
y.addpages(x.pages)
y.write(uploaded_file)

