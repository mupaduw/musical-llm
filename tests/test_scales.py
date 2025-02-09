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

if __name__ == '__main__':
    unittest.main()