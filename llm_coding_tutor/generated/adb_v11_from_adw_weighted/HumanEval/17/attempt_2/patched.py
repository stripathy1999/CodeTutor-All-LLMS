def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o|.| o| o|.|.|.|.| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Split the input string by spaces to get individual notes
    notes = music_string.split()
    
    # Initialize a list to store the number of beats for each note
    beats_per_note = []
    
    # Iterate over each note
    for note in notes:
        # Check if the note is a whole note ('o')
        if note == 'o':
            # Append 4 to the list since it lasts four beats
            beats_per_note.append(4)
        # Check if the note is a half note ('o|')
        elif note == 'o|':
            # Append 2 to the list since it lasts two beats
            beats_per_note.append(2)
        # Check if the note is a qu