import webbrowser
import tkinter as tk
from tkinter import messagebox

# Ana pencere oluşturma
root = tk.Tk()
root.title("MetaSh*t Fixer")
root.geometry("300x100")  # 10x500 çok dar olduğu için 300x200 olarak güncelledim

def arama_func():
    # Text widget'ından veriyi al ("end-1c" son satırdaki boşluğu almamak içindir)
    text = textbox.get("1.0", "end-1c")
    
    # Boş arama yapmayı engellemek için kontrol
    if text.strip(): 
        webbrowser.open("https://10.58.12.6:1081/incele?id=" + text)
    else:
        messagebox.showwarning("Eksik Bilgi", "Lütfen geçerli bir TC kimlik numarası giriniz.")

# Widget'ları oluşturma
# Arama genellikle tek satır olduğu için Entry de kullanılabilir ama Text istendiği için Text kullandım.
textbox = tk.Text(root, height=1, width=30) 
button = tk.Button(root, text="Röntgeni Göster", command=arama_func)

# Yerleştirme (Grid veya Pack kullanılabilir, burada düzenli durması için pack kullandım)
textbox.pack(pady=10, padx=10)
button.pack(pady=10)

root.mainloop()