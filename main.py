import tkinter as tk
from file_ops.save import save_file
from formatting.formatting import toggle_bold, toggle_italic
from symbols.symbols import show_symbols
from reactions.reactions import balance_reaction

root = tk.Tk()
root.title("Edytor naukowy z możliwością symulacji reakcji chemicznych")
root.geometry("800x600")

text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
text_area.pack(expand=True, fill="both")

text_area.tag_configure("bold", font=("Arial", 12, "bold"))
text_area.tag_configure("italic", font=("Arial", 12, "italic"))

menu = tk.Menu(root)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Zapisz", command=lambda: save_file(text_area))
menu.add_cascade(label="Plik", menu=file_menu)

format_menu = tk.Menu(menu, tearoff=0)
format_menu.add_command(label="Pogrubienie", command=lambda: toggle_bold(text_area))
format_menu.add_command(label="Kursywa", command=lambda: toggle_italic(text_area))
menu.add_cascade(label="Formatowanie", menu=format_menu)

symbol_menu = tk.Menu(menu, tearoff=0)
symbol_menu.add_command(label="Wstaw symbol", command=lambda: show_symbols(root, text_area))
menu.add_cascade(label="Symbole", menu=symbol_menu)

reaction_menu = tk.Menu(menu, tearoff=0)
reaction_menu.add_command(label="Zbilansuj reakcje", command=lamda: balance_reaction(text_area))
menu.add_cascade(label="Reakcje", menu=reaction_menu)

root.config(menu=menu)
root.mainloop()
