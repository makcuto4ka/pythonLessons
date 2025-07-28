import camelot
import pandas as pd

# 1. Путь к вашему PDF
pdf_path = 'table.pdf'

# 2. Считываем таблицы со всех страниц
#    flavor='stream' лучше подходит для «свободных» таблиц без чётких линий,
#    flavor='lattice' — если у таблицы чёткие границы ячеек.
tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')

# 3. Объединяем все найденные таблицы в один DataFrame
df = pd.concat([t.df for t in tables], ignore_index=True)

# 4. Опционально: задаём первую строку как заголовок
df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)

# 5. Сохраняем в Excel
df.to_excel('output_table.xlsx', index=False, engine='openpyxl')

print("Готово! Файл сохранён как output_table.xlsx")
