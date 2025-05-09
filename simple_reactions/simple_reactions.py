import tkinter as tk

simple_reactions = {
    "H₂ + O₂": "H₂O",
    "Na + Cl₂": "NaCl",
    "C + O₂": "CO₂",
    "Fe + O₂": "Fe₂O₃",
    "CH₄ + 2 O₂": "CO₂ + 2 H₂O",
    "HCl + NaOH": "NaCl + H₂O",
    "2 H₂O": "2 H₂ + O₂",
    "4 Fe + 3 O₂ + 6 H₂O": "4 Fe(OH)₃",
    "CH₃COOH + NaHCO₃": "CH₃COO⁻ + CO₂ + H₂O",
    "CO₂ + 6 H₂O + światło": "C₆H₁₂O₆ + 6 O₂",
    "C₆H₁₂O₆ + 6 O₂": "6 CO₂ + 6 H₂O + energia",
    "CaCO₃": "CaO + CO₂",
    "Ca(OH)₂ + CO₂": "CaCO₃ + H₂O",
    "NH₃ + H₂O": "NH₄⁺ + OH⁻",
    "S + O₂": "SO₂",
    "C₂H₅OH + 3 O₂": "2 CO₂ + 3 H₂O",
}

def show_simple_reactions(root, text_widget):
    top = tk.Toplevel(root)
    top.title("Wstaw prostą reakcję")

    listbox = tk.Listbox(top, width=30, height=10, font=("Arial", 14))
    for subs in simple_reactions:
        listbox.insert(tk.END, subs)
    listbox.pack(padx=10, pady=10)

    def insert_selected():
        sel = listbox.curselection()
        if sel:
            subs = listbox.get(sel[0])
            prod = simple_reactions[subs]
            text_widget.insert(tk.INSERT, f"{subs} → {prod}")
            top.destroy()

    tk.Button(top, text="Wstaw reakcję", command=insert_selected).pack(pady=5)