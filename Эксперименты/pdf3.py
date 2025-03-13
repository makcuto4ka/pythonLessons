import fitz  

def merge_to_vertical_column(input_path, output_path):
    src_doc = fitz.open(input_path)
    dst_doc = fitz.open()
    total_height = sum(page.rect.height for page in src_doc)
    max_width = max(page.rect.width for page in src_doc)
    new_page = dst_doc.new_page(width=max_width, height=total_height)
    y_offset = 0
    
    for page in src_doc:
        rect = fitz.Rect(0, y_offset, max_width, y_offset + page.rect.height)
        new_page.show_pdf_page(
            rect,
            src_doc,  
            page.number
        )
        y_offset += page.rect.height
    dst_doc.save(output_path)
    src_doc.close()
    dst_doc.close()
for i in range(1,8):
    
    if __name__ == "__main__":
        merge_to_vertical_column(
            f"5050_f_41_lekcii-po-lineinoi-algebre (1) (pdf.io) ({i}).pdf",
            f"output_vector{i}.pdf"
        )


