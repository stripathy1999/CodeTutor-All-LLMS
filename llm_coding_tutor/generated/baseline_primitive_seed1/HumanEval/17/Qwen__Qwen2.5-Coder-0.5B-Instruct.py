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
    parsed_notes = []
    for char in music_string:
        if char == 'o':
            parsed_notes.append(4)
        elif char == 'o|':
            parsed_notes.append(2)
        elif char == '.'|:
            parsed_notes.append(1)
    return parsed_notes

# test the function with provided data points
assert parse_music('o o|.| o| o|.|.|.|.| o o') == [