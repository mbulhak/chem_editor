import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from file_ops.save import open_file, save_file


class FileOperationsTests(unittest.TestCase):
    def test_utf8_save_and_open(self):
        text = 'Zażółć gęślą jaźń: H₂ + O₂ → H₂O'
        with tempfile.TemporaryDirectory() as directory:
            path = str(Path(directory) / 'reaction.txt')
            widget = Mock()
            widget.get.return_value = text
            with patch('file_ops.save.filedialog.asksaveasfilename', return_value=path), patch('file_ops.save.messagebox.showinfo'):
                save_file(widget)
            self.assertEqual(Path(path).read_text(encoding='utf-8'), text)
            widget.get.assert_called_once_with('1.0', 'end-1c')
            with patch('file_ops.save.filedialog.askopenfilename', return_value=path) as dialog:
                open_file(widget)
            self.assertIn('filetypes', dialog.call_args.kwargs)
            widget.insert.assert_called_once_with('1.0', text)

    def test_cancelled_dialogs_leave_editor_unchanged(self):
        widget = Mock()
        with patch('file_ops.save.filedialog.asksaveasfilename', return_value=''), patch('file_ops.save.filedialog.askopenfilename', return_value=''):
            save_file(widget)
            open_file(widget)
        self.assertEqual(widget.mock_calls, [])

    def test_invalid_utf8_preserves_editor(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'invalid.txt'
            path.write_bytes(b'\xff')
            widget = Mock()
            with patch('file_ops.save.filedialog.askopenfilename', return_value=str(path)), patch('file_ops.save.messagebox.showerror') as error:
                open_file(widget)
            error.assert_called_once()
            widget.delete.assert_not_called()

    def test_write_error_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            widget = Mock()
            with patch('file_ops.save.filedialog.asksaveasfilename', return_value=directory), patch('file_ops.save.messagebox.showerror') as error:
                save_file(widget)
            error.assert_called_once()
