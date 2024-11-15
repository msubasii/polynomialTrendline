import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

# CSV dosyasını seçip dönüştürme işlemini başlatan işlev
def dosya_sec_ve_donustur():
    # Kullanıcıdan dosya seçmesini iste
    file_path = filedialog.askopenfilename(
        title="CSV Dosyasını Seç",
        filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")]
    )
    
    if not file_path:  # Dosya seçilmediyse işlem yapma
        return

    try:
        # Dosyayı aç ve işleme başla
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Satırları işle
        data = []
        for line in lines:
            row = line.strip().split(',')
            row = [cell.replace('.', ',').replace('"', '') for cell in row]
            data.append(row)

        # Data'yı DataFrame'e dönüştür
        df = pd.DataFrame(data)

        # Çıktı dosyasını kaydet
        output_file = filedialog.asksaveasfilename(
            title="Excel Dosyasını Kaydet",
            defaultextension=".xlsx",
            filetypes=[("Excel Dosyaları", "*.xlsx")]
        )
        if output_file:
            df.to_excel(output_file, index=False, header=False)
            messagebox.showinfo("Başarılı", "Dönüştürme tamamlandı!")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("CSV to Excel Dönüştürücü")
pencere.geometry("400x200")

# Talimat metni
talimat = tk.Label(pencere, text="Bir CSV dosyası seçin ve Excel'e dönüştürün", font=("Arial", 12))
talimat.pack(pady=20)

# Buton
buton = tk.Button(pencere, text="CSV Dosyasını Seç ve Dönüştür", command=dosya_sec_ve_donustur)
buton.pack(pady=10)

# Ana döngüyü başlat
pencere.mainloop()
