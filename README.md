# Chem Editor

A desktop chemical text editor written in Python. This personal project combines chemical technology knowledge with GUI programming and integration of chemistry libraries. The interface is in Polish.

## Features

- Edit text with bold/italic formatting, undo/redo and chemical symbols.
- Insert common chemical formulas and example reactions.
- Balance reaction equations using ChemPy.
- Visualise molecular structures from SMILES notation using RDKit and Pillow.
- Open and save UTF-8 plain-text files.
- Switch between light and dark themes.

## Setup

Use Python 3.11 or 3.12 with Tkinter and a desktop display.

```bash
git clone https://github.com/mbulhak/chem_editor.git
cd chem_editor
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate
```

Install dependencies and run:

```bash
python -m pip install -r requirements.txt
python main.py
```

Tkinter is a Python system component, not a pip dependency. On Ubuntu/Debian, install `python3-tk` if your Python installation lacks it. A graphical desktop is required to launch the editor.

## Usage

For reaction balancing, enter or select an equation such as `H2 + O2 -> H2O` and choose **Reakcje → Zbilansuj reakcje**. Unicode subscripts and arrows are supported. Existing coefficients are ignored when recalculating the balance.

For molecular visualisation, enter a **SMILES string**, such as `CCO` for ethanol or `c1ccccc1` for benzene, in the SMILES field and press Enter. Molecular formulas such as `C2H6O` are not SMILES strings.

Use **Plik → Zapisz / Otwórz** for plain-text files. Formatting tags are not preserved in `.txt` files.

## Scope and limitations

This is an educational editor, not a reaction simulator or a validated scientific analysis tool. Example reactions are templates; the application does not predict products. Balancing uses chemical formulas with `+` separators; ionic charge notation containing `+` is not supported. The current editor does not warn about unsaved changes before opening another file or closing the window.

## Project structure

- `main.py`: GUI, menus, shortcuts and theme switching.
- `file_ops/`: UTF-8 text import/export.
- `formatting/`, `symbols/`: text formatting and chemical symbols.
- `compounds/`, `simple_reactions/`: formula and reaction templates.
- `reactions/`: input normalisation and reaction balancing.
- `structures/`: SMILES parsing and molecular visualisation.
- `tests/`: regression tests that do not require a display.

## Tests

After installing dependencies:

```bash
python -m unittest discover -s tests -v
```
