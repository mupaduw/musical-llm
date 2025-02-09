from music_theory.scales import Scale

def test_major_scale():
    major_c = Scale.major('C')
    assert major_c.get_notes() == ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
    
    major_d = Scale.major('D')
    assert major_d.get_notes() == ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D']

def test_major_scale_lowercase():
    major_c = Scale.major('c')
    assert major_c.get_notes() == ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
    
    major_d = Scale.major('d')
    assert major_d.get_notes() == ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D']

def test_major_scale_invalid_note():
    try:
        Scale.major('X')
    except ValueError as e:
        assert str(e) == "Invalid note: X"

def test_minor_natural_scale():
    natural_a = Scale.minor_natural('A')
    assert natural_a.get_notes() == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A']

def test_minor_harmonic_scale():
    harmonic_a = Scale.minor_harmonic('A')
    assert harmonic_a.get_notes() == ['A', 'B', 'C', 'D', 'E', 'F', 'G#', 'A']

def test_minor_melodic_scale():
    melodic_a_asc, melodic_a_desc = Scale.minor_melodic('A')
    assert melodic_a_asc.get_notes() == ['A', 'B', 'C', 'D', 'E', 'F#', 'G#', 'A']
    assert melodic_a_desc.get_notes() == ['A', 'G', 'F', 'E', 'D', 'C', 'B', 'A']