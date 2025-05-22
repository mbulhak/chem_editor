import tkinter as tk
from file_ops.save import save_file, open_file
from formatting.formatting import toggle_bold, toggle_italic
from symbols.symbols import show_symbols
from reactions.reactions import balance_reaction
from structures.structures import show_structure
from compounds.compounds import show_compounds
from simple_reactions.simple_reactions import show_simple_reactions

root = tk.Tk()
root.title("Edytor naukowy z możliwością symulacji reakcji chemicznych")
root.geometry("800x600")

current_theme = "light"

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

text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12), undo=True)
text_area.pack(expand=True, fill="both", padx=5, pady=5)

text_area.bind("<Control-z>", lambda e: text_area.edit_undo())
text_area.bind("<Control-y>", lambda e: text_area.edit_undo())

text_area.tag_configure("bold", font=("Arial", 12, "bold"))
text_area.tag_configure("italic", font=("Arial", 12, "italic"))

menu = tk.Menu(root)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Zapisz", command=lambda: save_file(text_area))
file_menu.add_command(label="Otwórz", command=lambda:open_file(text_area))
menu.add_cascade(label="Plik", menu=file_menu)

edit_menu = tk.Menu(menu, tearoff=0)
edit_menu.add_command(label="Cofnij   Ctrl+Z", command=lambda: text_area.edit_undo())
edit_menu.add_command(label="Ponów   Ctrl+Y", command=lambda: text_area.edit_undo())
menu.add_cascade(label="Edycja", menu=edit_menu)

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

cmp_menu = tk.Menu(menu, tearoff=0)
cmp_menu.add_command(label="Wstaw związek chemiczny", command=lambda: show_compounds(root, text_area))
menu.add_cascade(label="Związki", menu=cmp_menu)

react2_menu = tk.Menu(menu, tearoff=0)
react2_menu.add_command(
    label="Wstaw prostą reakcję",
    command=lambda:show_simple_reactions(root, text_area)
)
menu.add_cascade(label="Reakcje proste", menu=react2_menu)

def toggle_theme():
    global current_theme
    if current_theme == "light":
        root.configure(bg="black")
        text_area.configure(bg="black", fg="white", insertbackground="white")
        smiles_frame.configure(bg="black")
        smiles_entry.configure(bg="gray30", fg="white", insertbackground="white")
        current_theme = "dark"
    else:
        root.configure(bg="SystemButtonFace")
        text_area.configure(bg="white", fg="black", insertbackground="black")
        smiles_frame.configure(bg=root["bg"])
        smiles_entry.configure(bg="white", fg="black", insertbackground="black")
        current_theme="light"

view_menu = tk.Menu(menu, tearoff=0)
view_menu.add_command(label="Przełącz motyw", command=toggle_theme)
menu.add_cascade(label="Widok", menu=view_menu)

root.config(menu=menu)
root.mainloop()
