import tkinter as tk
from tkinter import ttk

class AplikasiPrediksiProdi:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Prediksi Prodi")
        self.root.geometry("400x600")
        self.root.configure(bg="violet")
        
        # Judul
        judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", 
                        font=("Arial", 14, "bold"))
        judul.pack(pady=20)
        
        # Frame untuk input nilai
        input_frame = ttk.Frame(root)
        input_frame.pack(padx=20, pady=10)
        
        # Daftar mata pelajaran
        self.mata_pelajaran = [
            "Matematika", "Bahasa Indonesia", "Bahasa Inggris", 
            "Fisika", "Kimia", "Biologi", "Sejarah", 
            "Geografi", "Ekonomi", "Sosiologi"
        ]
        
        # Dictionary untuk menyimpan Entry widget
        self.entries = {}
        
        # Membuat input fields
        for i, mapel in enumerate(self.mata_pelajaran):
            # Label mata pelajaran
            label = ttk.Label(input_frame, text=f"Nilai {mapel}:")
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            
            # Entry untuk nilai
            entry = ttk.Entry(input_frame, width=10)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[mapel] = entry
        
        # Button Prediksi
        self.btn_prediksi = ttk.Button(root, text="Hasil Prediksi", 
                                     command=self.prediksi)
        self.btn_prediksi.pack(pady=20)
        
        # Label hasil
        self.label_hasil = ttk.Label(root, text="", font=("Arial", 12))
        self.label_hasil.pack(pady=10)
        
    def prediksi(self):
        # Fungsi ini akan selalu mengembalikan "Teknologi Informasi"
        self.label_hasil.config(text="Teknologi Informasi")

# Membuat dan menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPrediksiProdi(root)

    root.mainloop()