import tkinter as tk

compounds = {
    "Woda (H₂O)": "H2O",
    "Dwutlenek węgla (CO₂)": "CO2",
    "Tlen (O₂)": "O2",
    "Azot (N₂)":"N2",
    "Chlorek sodu (NaCl)": "NaCl",
    "Glukoza (C₆H₁₂O₆)": "C(C1C(C(C(C(O1)O)O)O)O)O",
    "Etanol (C₂H₅OH)": "CCO",
    "Amoniak (NH₃)": "NH3",
    "Kwas siarkowy (H₂SO₄)": "H2SO4",
    "Kwas solny (HCl)": "HCl",
    "Wodorotlenek sodu (NaOH)": "NaOH",
    "Metan (CH₄)": "CH4",
    "Kwas octowy (CH₃COOH)": "CH4COOH",
    "Tlenek węgla (CO)": "CO",
    "Węglan wapnia (CaCO₃)": "CaCO3",
    "Wodorotlenek wapnia (CaOH)₂": "(CaOH)2",
    "Siarczan wapnia (CaSO₄)": "CaSO4",
    "Kwas azotowy (HNO₃)": "HNO3",
    "Aceton ((CH₃)₂CO)": "(CH3)2CO",
    "Dwutlenek siarki (SO₂)": "SO2"
}

def show_compounds(root, text_widget):
    top = tk.Toplevel(root)
    top.title("Wstaw związek chemiczny")

    listbox = tk.Listbox(top, width=30, height=15, font=("Arial", 14))
    for name in compounds:
        listbox.insert(tk.END, name)
    listbox.pack(padx=10, pady=10)

    def insert_selected():
        sel = listbox.curselection()
        if sel:
            idx = sel[0]
            name = listbox.get(idx)
            smiles = compounds[name]
            text_widget.insert(tk.INSERT, smiles)
            top.destroy()

    tk.Button(top, text="Wstaw", command=insert_selected).pack(pady=5)

