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

def toggle_bold():
    try:
        current_tags = text_area.tag_names("sel.first")
        if "bold" in current_tags:
            text_area.tag_remove("bold", "sel.first", "sel.last")
        else:
            text_area.tag_add("bold", "sel.first", "sel.last")
    except tk.TclError:
        messagebox.showwarning("Uwaga", "Zaznacz tekst, który chcesz pogrubić")

def toggle_italic():
    try:
        current_tags = text_area.tag_names("sel.first")
        if "italic" in current_tags:
            text_area.tag_remove("italic", "sel.first", "sel.last")
        else:
            text_area.tag_add("italic", "sel.first", "sel.last")
    except tk.TclError:
        messagebox.showwarning("Uwaga", "Zaznacz tekst, który chcesz pochylić")

root = tk.Tk()
root.title("Edytor naukowy z możliwością symulacji reakcji chemicznych")
root.geometry("800x600")

text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
text_area.pack(expand=True, fill="both")

text_area.tag_configure("bold", font=("Arial", 12, "bold"))
text_area.tag_configure("italic", font=("Arial", 12, "italic"))

menu = tk.Menu(root)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Zapisz", command=save_file)
menu.add_cascade(label="Plik", menu=file_menu)

format_menu = tk.Menu(menu, tearoff=0)
format_menu.add_command(label="Pogrubienie", command=toggle_bold)
format_menu.add_command(label="Kursywa", command=toggle_italic)
menu.add_cascade(label="Formatowanie", menu=format_menu)

root.config(menu=menu)
root.mainloop()
