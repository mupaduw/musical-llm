import unittest
from music_theory.scales import MajorScale, MinorScale

class TestScales(unittest.TestCase):

    def test_major_scale(self):
        major_c = MajorScale.create('C')
        self.assertEqual(major_c.get_notes(), ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'])

    def test_minor_natural_scale(self):
        minor_a = MinorScale.create_natural('A')
        self.assertEqual(minor_a.get_notes(), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'])

    def test_minor_harmonic_scale(self):
        harmonic_a = MinorScale.create_harmonic('A')
        self.assertEqual(harmonic_a.get_notes(), ['A', 'B', 'C', 'D', 'E', 'F', 'G#', 'A'])

    def test_minor_melodic_scale_ascending(self):
        melodic_a_asc, _ = MinorScale.create_melodic('A')
        self.assertEqual(melodic_a_asc.get_notes(), ['A', 'B', 'C', 'D', 'E', 'F#', 'G#', 'A'])

    def test_minor_melodic_scale_descending(self):
        _, melodic_a_desc = MinorScale.create_melodic('A')
        self.assertEqual(melodic_a_desc.get_notes(), ['A', 'G', 'F', 'E', 'D', 'C', 'B', 'A'])

    def test_relative_minor_key_major_c(self):
        self.assertEqual(MajorScale.create('C').root, MinorScale.create_harmonic('A').relative_major().root)

    def test_relative_major_key_minor_a(self):
        self.assertEqual(MinorScale.create_harmonic('A').root, MajorScale.create('C').relative_minor_key().root)

    # New tests for ascending argument
    def test_major_scale_ascending_true(self):
        major_c = MajorScale.create('C')
        self.assertEqual(major_c.get_notes(ascending=True), ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'])

    def test_major_scale_ascending_false(self):
        major_c = MajorScale.create('C')
        self.assertEqual(major_c.get_notes(ascending=False), ['C', 'B', 'A', 'G', 'F', 'E', 'D', 'C'])

    def test_minor_natural_scale_ascending_true(self):
        minor_a = MinorScale.create_natural('A')
        self.assertEqual(minor_a.get_notes(ascending=True), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'])

    def test_minor_natural_scale_ascending_false(self):
        minor_a = MinorScale.create_natural('A')
        self.assertEqual(minor_a.get_notes(ascending=False), [note for note in reversed(minor_a.get_notes())])
