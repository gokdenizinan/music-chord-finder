"""
Music Chord Finder - v1

Goal:
Identify basic chords from note names.

Supported in v1:
- Major chords
- Minor chords
- Diminished chords
- Augmented chords
- Inversions
- Sharp notes only
"""


NOTE_VALUES = {
    "C": 0,
    "C#": 1,
    "D": 2,
    "D#": 3,
    "E": 4,
    "F": 5,
    "F#": 6,
    "G": 7,
    "G#": 8,
    "A": 9,
    "A#": 10,
    "B": 11,

}


CHORD_PATTERNS = {
     "major": [0, 4, 7],
     "minor": [0, 3, 7],
     "diminished": [0, 3, 6],
     "augmented": [0, 4, 8]
}


def normalize_note(note): # one note at a time
    if len(note) == 1:
        note = note.upper()
    else:
        note = note[0].upper() + note[1]
    return note

def parse_user_input(user_input): #C E G#
    return user_input.split()

def notes_to_numbers(notes): # Convert valid note names into chromatic numbers.
    values = []
    for note in notes:
        if note not in NOTE_VALUES:
            return "Invalid note!"
        else:
            values.append(NOTE_VALUES[note])
    return values

def get_intervals(note_numbers, root_number):
    pass


def match_chord(intervals):
    pass


def find_possible_chords(notes):
    pass


def format_chord_name(root_note, chord_type):
    pass


def print_results(results):
    pass


def main():
    print("Welcome to Chord Finder!")
    user_input = input("Enter notes: ")

    print(parse_user_input(user_input))

    sep_input = parse_user_input(user_input)

    i = 0
    for note in sep_input:
        sep_input[i] = normalize_note(note)
        i+=1
    print(sep_input)

    print(notes_to_numbers(sep_input))



if __name__ == "__main__":
    main()