import re
import tkinter as tk
from tkinter import messagebox
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
            out.append(f"{coeff} {_subscript_formula(form)}")
        else:
            out.append(_subscript_formula(term))
    return " + ".join(out)

def parse_reaction(reaction):
    """Return formulas on both sides, ignoring existing stoichiometric coefficients."""
    reaction = convert_unicode_subscripts(reaction.strip())
    if reaction.count("->") + reaction.count("<-") != 1:
        raise ValueError("Podaj jedną reakcję ze strzałką ->, →, ← lub ⇌.")
    if "<-" in reaction:
        right, left = reaction.split("<-")
    else:
        left, right = reaction.split("->")

    def formulas(side):
        terms = [re.sub(r"^\d+\s*", "", term.strip()) for term in side.split("+")]
        if not all(terms):
            raise ValueError("Obie strony reakcji muszą zawierać poprawne wzory związków.")
        return set(terms)

    return formulas(left), formulas(right)


def balance_reaction(text_widget):
    try:
        try:
            reaction = text_widget.get("sel.first", "sel.last").strip()
        except tk.TclError:
            reaction = text_widget.get("1.0","end").strip()

        reaction = convert_unicode_subscripts(reaction)

        lhs, rhs = parse_reaction(reaction)

        balanced = balance_stoichiometry(lhs, rhs)
        lhs_bal = ' + '.join(f"{v} {k}" for k, v in balanced[0].items())
        rhs_bal = ' + '.join(f"{v} {k}" for k, v in balanced[1].items())

        lhs_fmt = _format_side(lhs_bal)
        rhs_fmt = _format_side(rhs_bal)

        result = f"Zbilansowana reakcja:\n{lhs_fmt} → {rhs_fmt}"
        messagebox.showinfo("Wynik bilansowania", result)

    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się zbilansować:\n{e}")
