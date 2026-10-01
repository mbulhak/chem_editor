"""Plain-text import and export for the editor."""
from tkinter import filedialog, messagebox

FILE_TYPES = [("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")]


def save_file(text_widget):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=FILE_TYPES
    )
    if not file_path:
        return
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            # Tk adds a newline that is not part of the document.
            file.write(text_widget.get("1.0", "end-1c"))
    except (OSError, UnicodeError) as error:
        messagebox.showerror("Błąd", f"Nie udało się zapisać pliku:\n{error}")
        return
    messagebox.showinfo("Zapisano", "Plik został zapisany.")


def open_file(text_widget):
    file_path = filedialog.askopenfilename(
        defaultextension=".txt", filetypes=FILE_TYPES
    )
    if not file_path:
        return
    try:
        # Failed reads must leave the editor unchanged.
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except (OSError, UnicodeError) as error:
        messagebox.showerror("Błąd", f"Nie udało się wczytać pliku:\n{error}")
        return
    text_widget.delete("1.0", "end")
    text_widget.insert("1.0", content)
