# Constants
HALF_STEP = 1
WHOLE_STEP = 2
AUGMENTED_SECOND = 3

# Function to convert note number to letter (e.g., 0 -> 'C', 1 -> 'C#', etc.)
def note_to_letter(note_number):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return notes[note_number % 12]

# Function to convert letter note to number (e.g., 'C' -> 0, 'C#' -> 1, etc.)
def letter_to_note(note_letter):
    notes = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
    return notes.get(note_letter.upper(), None)

class Scale:
    def __init__(self, notes):
        self.notes = notes

    @classmethod
    def major(cls, root):
        # Start with the root note number
        start_note = letter_to_note(root.upper())

        if start_note is None:
            raise ValueError(f"Invalid note: {root}")
        
        # Define the intervals for a major scale: W, W, H, W, W, W, H
        intervals = [WHOLE_STEP, WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, WHOLE_STEP, HALF_STEP]
        
        # Generate the notes of the scale based on the intervals
        notes = []
        current_note = start_note
        for i in range(8):  # Major scale has 7 distinct pitches + an octave
            if i == 0:
                notes.append(current_note)
            else:
                current_note += intervals[i - 1]
                notes.append(current_note)
        
        return cls(notes)

    @classmethod
    def minor_natural(cls, root):
        # Start with the root note number
        start_note = letter_to_note(root)

        if start_note is None:
            raise ValueError(f"Invalid note: {root}")

        # Define the intervals for a natural minor scale: W, H, W, W, H, W, W
        intervals = [WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP]
        
        # Generate the notes of the scale based on the intervals
        notes = []
        current_note = start_note
        for i in range(8):  # Minor scale has 7 distinct pitches + an octave
            if i == 0:
                notes.append(current_note)
            else:
                current_note += intervals[i - 1]
                notes.append(current_note)
        
        return cls(notes)

    @classmethod
    def minor_harmonic(cls, root):
        # Start with the root note number
        start_note = letter_to_note(root)

        if start_note is None:
            raise ValueError(f"Invalid note: {root}")

        # Define the intervals for a harmonic minor scale: W, H, W, W, H, A2, H
        intervals = [WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, HALF_STEP, AUGMENTED_SECOND, HALF_STEP]
        
        # Generate the notes of the scale based on the intervals
        notes = []
        current_note = start_note
        for i in range(8):  # Minor scale has 7 distinct pitches + an octave
            if i == 0:
                notes.append(current_note)
            else:
                current_note += intervals[i - 1]
                notes.append(current_note)
        
        return cls(notes)

    @classmethod
    def minor_melodic(cls, root):
        # Start with the root note number
        start_note = letter_to_note(root)

        if start_note is None:
            raise ValueError(f"Invalid note: {root}")
    
        # Define the intervals for a melodic minor scale ascending: W, H, W, W, W, W, H
        intervals_asc = [WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, WHOLE_STEP, WHOLE_STEP, HALF_STEP]
        
        # Generate the notes of the scale based on the intervals for ascending
        notes_asc = []
        current_note = start_note
        for i in range(8):  # Minor scale has 7 distinct pitches + an octave
            if i == 0:
                notes_asc.append(current_note)
            else:
                current_note += intervals_asc[i - 1]
                notes_asc.append(current_note)
        
        # Define the intervals for a melodic minor scale descending: W, H, W, W, H, W, W
        intervals_desc = [WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP]

        # Generate the notes of the scale based on the intervals for descending
        notes_desc = []
        current_note = start_note
        for i in range(8):  # Minor scale has 7 distinct pitches + an octave
            if i == 0:
                notes_desc.append(current_note)
            else:
                current_note += intervals_desc[i - 1]
                notes_desc.append(current_note)
        
        return cls(notes_asc), cls(reversed(notes_desc))

    def get_notes(self):
        return [note_to_letter(note) for note in self.notes]

# Example usage
major_c = Scale.major('C')
print("Major C:", major_c.get_notes())

natural_minor_a = Scale.minor_natural('A')
print("Natural Minor A:", natural_minor_a.get_notes())

harmonic_minor_a = Scale.minor_harmonic('A')
print("Harmonic Minor A:", harmonic_minor_a.get_notes())

melodic_minor_a_asc, melodic_minor_a_desc = Scale.minor_melodic('A')
print("Melodic Minor A (Ascending):", melodic_minor_a_asc.get_notes())
print("Melodic Minor A (Descending):", melodic_minor_a_desc.get_notes())