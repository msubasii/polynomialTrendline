import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import os
import threading

class CSVtoExcelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Converter")
        self.center_window(400, 250)  # Pencereyi ortala
        self.root.configure(bg="#f5f5f5")  # Arka plan rengi

        # Başlık
        self.title_label = tk.Label(
            root, text="Excel Converter", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333"
        )
        self.title_label.pack(pady=20)

        # Talimat metni
        self.instruction_label = tk.Label(
            root, text="Bir CSV dosyasını Excel'e dönüştürün", font=("Arial", 12), bg="#f5f5f5", fg="#555"
        )
        self.instruction_label.pack(pady=10)

        # Buton
        self.select_button = ttk.Button(root, text="Excel'e Dönüştürülecek Dosyayı Seçin", command=self.start_conversion)
        self.select_button.pack(pady=20)

    def center_window(self, width, height):
        """Pencereyi ekranın ortasına yerleştir"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def start_conversion(self):
        # Dosya seçme işlemi
        self.file_path = filedialog.askopenfilename(
            title="Excel'e Dönüştürülecek Dosyayı Seçin",
            filetypes=[("Tüm Dosyalar", "*.*")]
        )
        if not self.file_path:
            return

        # Çıktı dosyası seçme
        self.output_file = filedialog.asksaveasfilename(
            title="Excel Dosyasını Kaydet",
            defaultextension=".xlsx",
            filetypes=[("Excel Dosyaları", "*.xlsx")]
        )
        if not self.output_file:
            return

        # Dönüştürme ekranına geçiş
        self.show_progress_screen()

        # Dönüştürme işlemini başlat
        threading.Thread(target=self.convert_file).start()

    def show_progress_screen(self):
        # Mevcut bileşenleri gizle
        for widget in self.root.winfo_children():
            widget.pack_forget()

        # Dönüştürme ekranını göster
        self.progress_label = tk.Label(self.root, text="Dönüştürülüyor...", font=("Arial", 14), bg="#f5f5f5", fg="#333")
        self.progress_label.pack(pady=30)

        self.progress_bar = ttk.Progressbar(self.root, mode='indeterminate', length=300)
        self.progress_bar.pack(pady=20)
        self.progress_bar.start(10)

    def convert_file(self):
        try:
            # Dosyayı aç ve işleme başla
            with open(self.file_path, 'r') as file:
                lines = file.readlines()

            # Satırları işle
            data = []
            for line in lines:
                row = line.strip().split(',')
                row = [cell.replace('.', ',').replace('"', '') for cell in row]
                data.append(row)

            # Data'yı DataFrame'e dönüştür ve kaydet
            df = pd.DataFrame(data)
            df.to_excel(self.output_file, index=False, header=False)

            # İşlem tamamlandı ekranına geçiş
            self.show_success_screen()
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")
            self.root.destroy()

    def show_success_screen(self):
        # Dönüştürme ekranını temizle
        for widget in self.root.winfo_children():
            widget.pack_forget()

        # Başarı ekranını göster
        self.success_label = tk.Label(
            self.root, text="Dönüştürme Tamamlandı!", font=("Arial", 14), bg="#f5f5f5", fg="green"
        )
        self.success_label.pack(pady=20)

        self.open_button = ttk.Button(self.root, text="Oluşan Dosyayı Aç", command=self.open_file)
        self.open_button.pack(pady=10)

    def open_file(self):
        try:
            os.startfile(self.output_file)  # Windows için varsayılan uygulamada açar
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya açılamadı: {e}")


# Uygulamayı başlat
if __name__ == "__main__":
    root = tk.Tk()
    app = CSVtoExcelApp(root)
    root.mainloop()