import io
import tkinter as tk
from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image, ImageTk


def show_structure(root, smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        tk.messagebox.showerror("Błąd", f"Niepoprawny SMILES:\n{smiles}")
        return

    img = Draw.MolToImage(mol, size=(300,300))

    bio = io.BytesIO()
    img.save(bio, "PNG")
    bio.seek(0)

    top = tk.Toplevel(root)
    top.title(f"Struktura: {smiles}")

    pil_img = Image.open(bio)
    tk_img = ImageTk.PhotoImage(pil_img)
    label = tk.Label(top, image=tk_img)
    label.image = tk_img
    label.pack(padx=10, pady=10)
