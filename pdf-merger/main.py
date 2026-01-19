from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("How many PDFs do you want to merge?: "))

for i in range(0, n):
    name = input(f"Enter the name of {i+1} PDF file (without .pdf extension): ")
    pdfs.append(name + ".pdf")

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
print("All provided PDFs have been merged into 'merged-pdf.pdf' successfully.")
merger.close()