import unittest
from unittest.mock import Mock, patch
import tkinter as tk
from rdkit import Chem
from rdkit.Chem import Draw
from structures.structures import show_structure
import main


class GuiCallbackTests(unittest.TestCase):
    def test_theme_and_history_callbacks(self):
        root = Mock()
        root.cget.return_value = '#eeeeee'
        text = Mock()
        text.edit_undo.side_effect = tk.TclError('nothing to undo')
        menus = []

        def menu(*args, **kwargs):
            instance = Mock()
            menus.append(instance)
            return instance

        with patch('main.tk.Tk', return_value=root), patch('main.tk.Text', return_value=text), patch('main.tk.Frame'), patch('main.tk.Label'), patch('main.tk.Entry'), patch('main.tk.Menu', side_effect=menu):
            main.main()
            commands = {call.kwargs['label']: call.kwargs['command'] for instance in menus for call in instance.add_command.call_args_list}
            commands['Przełącz motyw']()
            root.configure.assert_called_with(bg='black')
            commands['Przełącz motyw']()
            root.configure.assert_called_with(bg='#eeeeee')
            commands['Cofnij   Ctrl+Z']()
            commands['Ponów   Ctrl+Y']()
            text.edit_redo.assert_called_once()
            bindings = {call.args[0]: call.args[1] for call in text.bind.call_args_list}
            self.assertEqual(bindings['<Control-y>'](None), 'break')

    def test_empty_and_invalid_smiles_do_not_create_window(self):
        with patch('structures.structures.messagebox') as dialogs, patch('structures.structures.tk.Toplevel') as window:
            show_structure(Mock(), '   ')
            show_structure(Mock(), 'not-a-smiles')
            dialogs.showwarning.assert_called_once()
            dialogs.showerror.assert_called_once()
            window.assert_not_called()

    def test_real_molecule_rendering(self):
        molecule = Chem.MolFromSmiles('CCO')
        self.assertEqual(molecule.GetNumAtoms(), 3)
        self.assertEqual(Draw.MolToImage(molecule, size=(300, 300)).size, (300, 300))


if __name__ == '__main__':
    unittest.main()
