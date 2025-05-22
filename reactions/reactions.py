import re
import tkinter as tk
from tkinter import messagebox, TclError
from chempy import balance_stoichiometry

_SUB_MAP = {
    '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
    '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉',
}

def convert_unicode_subscripts(text):
    rev = {v: k for k, v in _SUB_MAP.items()}
    for uni, ascii_ in rev.items():
        text = text.replace(uni, ascii_)
    text = text.replace('→', '->').replace('←', '<-').replace('⇌', '->')
    return text

def _subscript_formula(formula: str) -> str:
    for arabic, uni in _SUB_MAP.items():
        formula = formula.replace(arabic, uni)
    return formula

def _format_side(side: str) -> str:
    terms = [t.strip() for t in side.split('+')]
    out = []
    for term in terms:
        m = re.match(r'^(\d+)\s*(.*)$', term)
        if m:
            coeff, form = m.groups()
            form_sub = _subscript_formula(form)
            out.append(f"{coeff} {_subscript_formula(form)}")
        else:
            out.append(_subscript_formula(term))
    return " + ".join(out)

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

        lhs_fmt = _format_side(lhs_bal)
        rhs_fmt = _format_side(rhs_bal)

        result = f"Zbilansowana reakcja:\n{lhs_fmt} → {rhs_fmt}"
        messagebox.showinfo("Wynik bilansowania", result)

    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się zbilansować:\n{e}")