import tkinter as tk
from tkinter import messagebox

def toggle_bold(text_widget):
    try:
        current_tags = text_widget.tag_names("sel.first")
        if "bold" in current_tags:
            text_widget.tag_remove("bold", "sel.first", "sel.last")
        else:
            text_widget.tag_add("bold", "sel.first", "sel.last")
    except tk.TclError:
        messagebox.showwarning("Uwaga", "Zaznacz tekst, który chcesz pogrubić")

def toggle_italic(text_widget):
    try:
        current_tags = text_widget.tag_names("sel.first")
        if "italic" in current_tags:
            text_widget.tag_remove("italic", "sel.first", "sel.last")
        else:
            text_widget.tag_add("italic", "sel.first", "sel.last")
    except tk.TclError:
        messagebox.showwarning("Uwaga", "Zaznacz tekst, który chcesz pochylić")