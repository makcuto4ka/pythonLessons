import fitz  # PyMuPDF
from reportlab.pdfgen import canvas
from io import BytesIO
import math
from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from io import BytesIO
import tempfile
import math

def merge_to_vertical_column(input_path, output_path):
    # Открываем PDF
    doc = fitz.open(input_path)
    
    # Получаем размеры первой страницы
    first_page = doc[0]
    page_width = first_page.rect.width
    page_height = first_page.rect.height
    
    # Рассчитываем общую высоту
    total_height = page_height * len(doc)
    
    # Создаем PDF с помощью ReportLab
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(page_width, total_height))
    
    # Размещаем страницы вертикально
    y_position = total_height - page_height
    for page in doc:
        pix = page.get_pixmap()
        img_data = pix.tobytes("png")
        img_reader = ImageReader(BytesIO(img_data))
        c.drawImage(img_reader, 0, y_position, width=page_width, height=page_height)
        y_position -= page_height
    
    c.save()
    
    # Сохраняем результат
    packet.seek(0)
    with open(output_path, "wb") as f:
        f.write(packet.getvalue())


if __name__ == "__main__":
    merge_to_vertical_column("5050_f_41_lekcii-po-lineinoi-algebre (1) (pdf.io).pdf", "output.pdf")

