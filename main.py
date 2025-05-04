import tkinter as tk
from tkinter import filedialog, messagebox

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_area.get("1.0", tk.END))
            messagebox.showinfo("Zapisano", "Plik został zapisany.")
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się zapisać pliku:\n{e}")

root = tk.Tk()
root.title("Edytor naukowy z możliwością symulacji reakcji chemicznych")
root.geometry("800x600")

text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
text_area.pack(expand=True, fill="both")

menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Zapisz", command=save_file)
menu.add_cascade(label="Plik", menu=file_menu)

root.config(menu=menu)
root.mainloop()
