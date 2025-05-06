from tkinter import messagebox, TclError

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