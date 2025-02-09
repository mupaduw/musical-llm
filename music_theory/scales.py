"""
support western scale theory

Examples:

    ```python

    # examples
    major_c = MajorScale.create('C')
    print("Major C:", major_c.get_notes())
    
    harmonic_minor_a = MinorScale.create_harmonic('A')
    print("Harmonic Minor A:", harmonic_minor_a.get_notes())

    melodic_minor_a_asc, melodic_minor_a_desc = MinorScale.create_melodic('A')
    print("Melodic Minor A (Ascending):", melodic_minor_a_asc.get_notes())
    print("Melodic Minor A (Descending):", melodic_minor_a_desc.get_notes())
    ```
"""

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
    """
    Represents a musical scale.
    
    Attributes:
        notes (list of int): The note numbers that make up the scale.
    """

    def __init__(self, notes):
        self.notes = notes

    def get_notes(self):
        """
        Returns the note letters for this scale.
        
        Returns:
            list of str: A list containing the note letters.
        """
        return [note_to_letter(note) for note in self.notes]

class MajorScale(Scale):
    """
    Represents a major musical scale.
    
    Inherits from Scale.
    """

    @classmethod
    def create(cls, root):
        """
        Creates a new instance of MajorScale with the given root note.
        
        Args:
            root (str): The root note for this scale (e.g., 'C', 'D#').
            
        Returns:
            MajorScale: A new MajorScale object.
        
        Raises:
            ValueError: If an invalid note is provided.
        """
        start_note = letter_to_note(root.upper())

        if start_note is None:
            raise ValueError(f"Invalid note: {root}")
        
        intervals = [WHOLE_STEP, WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, WHOLE_STEP, HALF_STEP]
        
        notes = []
        current_note = start_note
        for i in range(8):
            if i == 0:
                notes.append(current_note)
            else:
                current_note += intervals[i - 1]
                notes.append(current_note)
        
        return cls(notes)

class MinorScale(Scale):
    """
    Represents a minor musical scale.
    
    Inherits from Scale.
    """

    @classmethod
    def create_natural(cls, root):
        """
        Creates a new instance of MinorScale with the given natural minor root note.
        
        Args:
            root (str): The root note for this scale (e.g., 'A', 'C').
            
        Returns:
            MinorScale: A new MinorScale object.
        
        Raises:
            ValueError: If an invalid note is provided.
        """
        start_note = letter_to_note(root.upper())

        if start_note is None:
            raise ValueError(f"Invalid note: {root}")

        intervals = [WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP]
        
        notes = []
        current_note = start_note
        for i in range(8):
            if i == 0:
                notes.append(current_note)
            else:
                current_note += intervals[i - 1]
                notes.append(current_note)
        
        return cls(notes)

    @classmethod
    def create_harmonic(cls, root):
        """
        Creates a new instance of MinorScale with the given harmonic minor root note.
        
        Args:
            root (str): The root note for this scale (e.g., 'A', 'C').
            
        Returns:
            MinorScale: A new MinorScale object.
        
        Raises:
            ValueError: If an invalid note is provided.
        """
        start_note = letter_to_note(root.upper())

        if start_note is None:
            raise ValueError(f"Invalid note: {root}")

        intervals = [WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, HALF_STEP, AUGMENTED_SECOND, HALF_STEP]
        
        notes = []
        current_note = start_note
        for i in range(8):
            if i == 0:
                notes.append(current_note)
            else:
                current_note += intervals[i - 1]
                notes.append(current_note)
        
        return cls(notes)

    @classmethod
    def create_melodic(cls, root):
        """
        Creates a new instance of MinorScale with the given melodic minor root note.
        
        Args:
            root (str): The root note for this scale (e.g., 'A', 'C').
            
        Returns:
            tuple: A tuple containing two MinorScale objects - one for ascending and one for descending.
        
        Raises:
            ValueError: If an invalid note is provided.
        """
        start_note = letter_to_note(root.upper())
        
        if start_note is None:
            raise ValueError(f"Invalid note: {root}")
    
        intervals_asc = [WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, WHOLE_STEP, WHOLE_STEP, HALF_STEP]
        
        notes_asc = []
        current_note = start_note
        for i in range(8):
            if i == 0:
                notes_asc.append(current_note)
            else:
                current_note += intervals_asc[i - 1]
                notes_asc.append(current_note)

        intervals_desc = [WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP, HALF_STEP, WHOLE_STEP, WHOLE_STEP]

        notes_desc = []
        current_note = start_note
        for i in range(8):
            if i == 0:
                notes_desc.append(current_note)
            else:
                current_note += intervals_desc[i - 1]
                notes_desc.append(current_note)
        
        return cls(notes_asc), cls(reversed(notes_desc))

    def relative_major_key(self):
        """
        Returns the relative major key for this minor scale.
        
        Returns:
            str: The relative major key as a string (e.g., 'C#', 'Eb').
        """
        # Define a dictionary to map each minor key to its corresponding relative major key
        relative_majors = {
            'A': 'C#',
            'A#': 'D#',
            'B': 'E',
            'C': 'Eb',
            'C#': 'F',
            'D': 'F#',
            'D#': 'G#',
            'E': 'A',
            'F': 'Ab',
            'F#': 'Bb',
            'G': 'B',
            'G#': 'C'
        }

