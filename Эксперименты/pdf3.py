import fitz  # PyMuPDF

def merge_to_vertical_column(input_path, output_path):
    # Открываем исходный PDF
    src_doc = fitz.open(input_path)
    
    # Создаем новый PDF
    dst_doc = fitz.open()
    
    # Рассчитываем общие размеры
    total_height = sum(page.rect.height for page in src_doc)
    max_width = max(page.rect.width for page in src_doc)
    
    # Создаем новую страницу в целевом документе
    new_page = dst_doc.new_page(width=max_width, height=total_height)
    
    # Позиция для вставки (начинаем с верхней границы)
    y_offset = 0
    
    for page in src_doc:
        # Определяем область для вставки
        rect = fitz.Rect(0, y_offset, max_width, y_offset + page.rect.height)
        
        # Вставляем страницу как PDF-форму (XObject)
        new_page.show_pdf_page(
            rect,
            src_doc,  # исходный документ
            page.number  # номер страницы
        )
        
        # Увеличиваем смещение для следующей страницы
        y_offset += page.rect.height
    
    # Сохраняем результат
    dst_doc.save(output_path)
    src_doc.close()
    dst_doc.close()
for i in range(1,8):
    
    if __name__ == "__main__":
        merge_to_vertical_column(
            f"5050_f_41_lekcii-po-lineinoi-algebre (1) (pdf.io) ({i}).pdf",
            f"output_vector{i}.pdf"
        )


