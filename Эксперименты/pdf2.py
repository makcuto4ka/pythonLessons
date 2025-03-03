import fitz  # PyMuPDF
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.utils import ImageReader

def merge_to_vertical_column(input_path, output_path, dpi=600):
    # Открываем исходный PDF
    doc = fitz.open(input_path)
    
    # Получаем размеры первой страницы в пунктах (1/72 дюйма)
    first_page = doc[0]
    page_width = first_page.rect.width
    page_height = first_page.rect.height
    
    # Рассчитываем общую высоту нового документа
    total_height = page_height * len(doc)
    
    # Создаем PDF с помощью ReportLab
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(page_width, total_height))
    
    # Коэффициент масштабирования для увеличения DPI
    zoom = dpi / 72  # 72 - стандартный DPI PDF
    matrix = fitz.Matrix(zoom, zoom)
    
    # Размещаем страницы вертикально
    y_position = total_height - page_height  # Начинаем сверху
    
    for page in doc:
        # Рендерим страницу с повышенным DPI
        pix = page.get_pixmap(matrix=matrix)
        
        # Конвертируем в изображение
        img_data = pix.tobytes("png")
        img_reader = ImageReader(BytesIO(img_data))
        
        # Рассчитываем размеры с учетом масштабирования
        actual_width = page_width * zoom
        actual_height = page_height * zoom
        
        # Рисуем изображение с масштабированием до оригинальных размеров
        c.drawImage(
            img_reader,
            0,
            y_position,
            width=page_width,
            height=page_height,
            preserveAspectRatio=True,
            mask='auto'
        )
        y_position -= page_height
    
    c.save()
    
    # Сохраняем результат
    packet.seek(0)
    with open(output_path, "wb") as f:
        f.write(packet.getvalue())

if __name__ == "__main__":
    merge_to_vertical_column(
        "5050_f_41_lekcii-po-lineinoi-algebre (1) (pdf.io).pdf",
        "output2.pdf",
        dpi=600  # Можно увеличить до 600 для лучшего качества
    )

