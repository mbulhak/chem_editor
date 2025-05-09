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

def open_file(text_widget):
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetype=[("Pliki tekstowe","*txt"),("Wszystkie pliki","*.*")]
    )
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            text_widget.delete("1.0","end")
            text_widget.insert("1.0", content)
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się wczytać pliku:\n{e}")
