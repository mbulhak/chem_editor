import tkinter as tk

all_symbols = [
    "→", "⇌", "↔", "←", "+", "−", "⁺", "⁻",
    "₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉",
    "⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹",
]

def show_symbols():
    top = tk.Toplevel(root)
    top.title("Wstaw symbol")

    listbox = tk.Listbox(top, width=20, height=15, font=("Arial", 14))
    for sym in all_symbols:
        listbox.insert(tk.END, sym)
    listbox.pack(padx=10, pady=10)

    def insert_selected():
        selection = listbox.curselection()
        if selection:
            symbol = listbox.get(selection)
            text_widget.insert(tk.INSERT, symbol)
            top.destroy()

    insert_btn = tk.Button(top, text="Wstaw", command=insert_selected)
    insert_btn.pack(pady=5)

