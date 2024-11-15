import csv
import pandas as pd

# Metin dosyasını aç ve satırları oku
with open('input.txt', 'r') as file:
    # Satırları ayırarak bir listeye dönüştür
    lines = file.readlines()

# Satırları işleyerek her birini CSV formatına dönüştür
data = []
for line in lines:
    # Satırdaki her virgülü bir sütun olarak kabul et
    row = line.strip().split(',')
    
    # . yerine , koy ve " işaretlerini sil
    row = [cell.replace('.', ',').replace('"', '') for cell in row]
    data.append(row)

# Data'yı pandas DataFrame'e çevir
df = pd.DataFrame(data)

# DataFrame'i bir Excel dosyasına yaz
df.to_excel('output.xlsx', index=False, header=False)

