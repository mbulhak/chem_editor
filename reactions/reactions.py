import tkinter as tk
from tkinter import messagebox, TclError
from chempy import balance_stoichiometry

def convert_unicode_subscripts(text):
    subscript_map = {
        '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4',
        '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9'
    }
    for uni, num in subscript_map.items():
        text = text.replace(uni, num)

    text = text.replace('→', '->')
    text = text.replace('⇌', '->')
    text = text.replace('←', '<-')
    return text

def balance_reaction(text_widget):
    try:
        try:
            reaction = text_widget.get("sel.first", "sel.last").strip()
        except tk.TclError:
            reaction = text_widget.get("1.0","end").strip()

        reaction = convert_unicode_subscripts(reaction)

        if '->' not in reaction:
            messagebox.showwarning("Uwaga", "Reakcja musi zawierać '->'")
            return

        lhs_str, rhs_str = reaction.split("->")
        lhs = {s.strip() for s in lhs_str.split('+')}
        rhs = {s.strip() for s in rhs_str.split('+')}

        balanced = balance_stoichiometry(lhs, rhs)
        lhs_bal = ' + '.join(f"{v} {k}" for k, v in balanced[0].items())
        rhs_bal = ' + '.join(f"{v} {k}" for k, v in balanced[1].items())

        result = f"Zbilansowana reakcja:\n{lhs_bal} → {rhs_bal}"
        messagebox.showinfo("Wynik bilansowania", result)

    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się zbilansować:\n{e}")