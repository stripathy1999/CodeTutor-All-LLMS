def parse_music(music_string: str) -> List[int]:
    """ Parse a musical string and return the number of beats each not last.
    The ASCII format uses 'o', 'o|', and '.'| to represent whole, half, and quarter notes,
    respectively.
    
    Example:
    parse_music('o o|.| o| o|.|.|.|.| o o') -> [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Define the mapping of ASCII characters to their respective beats
    note_to_beats = {'o': 4, 'o|': 2, '.|': 1}
    
    # Split the input string into individual note strings
    note_strings = music_string.split()
    
    # Process each note string
    beats = [note_to_beats[note] for note in note_strings if note in note_to_beats]
    
    return beats