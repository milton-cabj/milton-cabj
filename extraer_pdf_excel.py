import fitz  # PyMuPDF
import openpyxl

# Abrir el PDF
pdf = fitz.open("factura.pdf")
texto = ""
for pagina in pdf:
    texto += pagina.get_text()
pdf.close()

# Crear Excel
wb = openpyxl.Workbook()
hoja = wb.active
hoja["A1"] = "Texto extraído del PDF:"
hoja["A2"] = texto

wb.save("resultado.xlsx")
print("✅ Hecho: se creó 'resultado.xlsx'")
