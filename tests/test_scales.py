import pytest
from music_theory.scales import MajorScale, MinorScale

def test_major_scale():
    major_c = MajorScale.create('C')
    assert major_c.get_notes() == ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

def test_minor_natural_scale():
    minor_a = MinorScale.create_natural('A')
    assert minor_a.get_notes() == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A']

def test_minor_harmonic_scale():
    harmonic_a = MinorScale.create_harmonic('A')
    assert harmonic_a.get_notes() == ['A', 'B', 'C', 'D', 'E', 'F', 'G#', 'A']

def test_minor_melodic_scale_ascending():
    melodic_a_asc, _ = MinorScale.create_melodic('A')
    assert melodic_a_asc.get_notes() == ['A', 'B', 'C', 'D', 'E', 'F#', 'G#', 'A']

def test_minor_melodic_scale_descending():
    _, melodic_a_desc = MinorScale.create_melodic('A')
    assert melodic_a_desc.get_notes() == ['A', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

def test_relative_minor_key_major_c():
    assert MajorScale.create('C').root == MinorScale.create_harmonic('A').relative_major().root

def test_relative_major_key_minor_a():
    assert MinorScale.create_harmonic('A').root == MajorScale.create('C').relative_minor_key().root

# New tests for ascending argument
def test_major_scale_ascending_true():
    major_c = MajorScale.create('C')
    assert major_c.get_notes(ascending=True) == ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']

def test_major_scale_ascending_false():
    major_c = MajorScale.create('C')
    assert major_c.get_notes(ascending=False) == ['C', 'B', 'A', 'G', 'F', 'E', 'D', 'C']

def test_minor_natural_scale_ascending_true():
    minor_a = MinorScale.create_natural('A')
    assert minor_a.get_notes(ascending=True) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A']

def test_minor_natural_scale_ascending_false():
    minor_a = MinorScale.create_natural('A')
    assert minor_a.get_notes(ascending=False) == [note for note in reversed(minor_a.get_notes())]
