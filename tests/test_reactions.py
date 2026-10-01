import unittest
from unittest.mock import Mock, patch
from reactions.reactions import parse_reaction, balance_reaction
from chempy import balance_stoichiometry


class ReactionTests(unittest.TestCase):
    def test_unicode_input_and_existing_coefficients(self):
        left, right = parse_reaction('2 H₂ + O₂ → 2 H₂O')
        self.assertEqual(left, {'H2', 'O2'})
        self.assertEqual(right, {'H2O'})
        lhs, rhs = balance_stoichiometry(left, right)
        self.assertEqual(dict(lhs), {'H2': 2, 'O2': 1})
        self.assertEqual(dict(rhs), {'H2O': 2})

    def test_left_and_equilibrium_arrows(self):
        self.assertEqual(parse_reaction('H₂O ← H₂ + O₂'), ({'H2', 'O2'}, {'H2O'}))
        self.assertEqual(parse_reaction('H₂ + O₂ ⇌ H₂O'), ({'H2', 'O2'}, {'H2O'}))

    def test_invalid_reactions(self):
        for text in ['', 'H2 + O2', '-> H2O', 'H2 + -> H2O', 'H2 -> H2O -> O2']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                parse_reaction(text)

    def test_selected_reaction_produces_result_dialog(self):
        widget = Mock()
        widget.get.return_value = 'H2 + O2 -> H2O'
        with patch('reactions.reactions.messagebox.showinfo') as result:
            balance_reaction(widget)
        self.assertIn('2 H₂O', result.call_args.args[1])
