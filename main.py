import tkinter as tk
from file_ops.save import save_file
from formatting.formatting import toggle_bold, toggle_italic
from symbols.symbols import show_symbols
from reactions.reactions import balance_reaction
from structures.structures import show_structure

root = tk.Tk()
root.title("Edytor naukowy z możliwością symulacji reakcji chemicznych")
root.geometry("800x600")

smiles_frame = tk.Frame(root)
smiles_frame.pack(fill="x", padx=5, pady=5)

smiles_label = tk.Label(smiles_frame, text="SMILES:")
smiles_label.pack(side="left")

placeholder = "np.CCO"

def on_focus_in(event):
    if smiles_entry.get() == placeholder:
        smiles_entry.delete(0, tk.END)
        smiles_entry.config(fg="black")

def on_focus_out(event):
    if not smiles_entry.get():
        smiles_entry.insert(0, placeholder)
        smiles_entry.config(fg="gray")

smiles_entry = tk.Entry(smiles_frame, width=30, fg="gray")
smiles_entry.pack(side="left", padx=5)
smiles_entry.insert(0, placeholder)

smiles_entry.bind("<FocusIn>", on_focus_in)
smiles_entry.bind("<FocusOut>", on_focus_out)

smiles_entry.bind(
    "<Return>",
    lambda event: show_structure(root, smiles_entry.get().strip())
)

text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
text_area.pack(expand=True, fill="both")

text_area.tag_configure("bold", font=("Arial", 12, "bold"))
text_area.tag_configure("italic", font=("Arial", 12, "italic"))

menu = tk.Menu(root)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Zapisz", command=lambda: save_file(text_area))
file_menu.add_command(label="Otwórz", command=lambda: None)
menu.add_cascade(label="Plik", menu=file_menu)

format_menu = tk.Menu(menu, tearoff=0)
format_menu.add_command(label="Pogrubienie", command=lambda: toggle_bold(text_area))
format_menu.add_command(label="Kursywa", command=lambda: toggle_italic(text_area))
menu.add_cascade(label="Formatowanie", menu=format_menu)

symbol_menu = tk.Menu(menu, tearoff=0)
symbol_menu.add_command(label="Wstaw symbol", command=lambda: show_symbols(root, text_area))
menu.add_cascade(label="Symbole", menu=symbol_menu)

reaction_menu = tk.Menu(menu, tearoff=0)
reaction_menu.add_command(label="Zbilansuj reakcje", command=lambda: balance_reaction(text_area))
menu.add_cascade(label="Reakcje", menu=reaction_menu)

root.config(menu=menu)
root.mainloop()
