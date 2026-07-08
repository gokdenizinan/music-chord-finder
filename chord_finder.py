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

"""
- [] Work on invalid cases, all others pass
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
     "maj": [0, 4, 7],
     "m": [0, 3, 7],
     "dim": [0, 3, 6],
     "aug": [0, 4, 8]
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

# Keep also inversion in mind: C E G and E G C are both C majors!

# Example Output:
""""
get_intervals([0, 4, 7], 0) → [0, 4, 7]
get_intervals([4, 7, 0], 0) → [0, 4, 7]
get_intervals([4, 7, 0], 4) → [0, 3, 8]
get_intervals([9, 0, 4], 9) → [0, 3, 7]
"""
def get_intervals(note_numbers, root_number): # Calculate the distances between each note and a possible root note
    interval = []
    for note in note_numbers:
        difference = note - root_number
        if difference < 0:
            difference+=12
        interval.append(difference)
    interval.sort()

    if interval in CHORD_PATTERNS.values():
        return interval
    else:
        return False

def match_chord(intervals):
    index = 0
    for pattern in CHORD_PATTERNS.keys(): # When we iterate through a list they become string
        if CHORD_PATTERNS[pattern] == intervals:
            return pattern
        index+=1
    return None

def find_possible_chords(notes):
    for root_number in notes:
        intervals = get_intervals(notes, root_number)
        if intervals != False:
            for note in NOTE_VALUES.keys():
                if NOTE_VALUES[note] == root_number:
                    chord_tuple = [note , match_chord(intervals)]
                    return chord_tuple          
            
def format_chord_name(root_note, chord_type):
    return root_note + chord_type


def print_results(results):
    print("Possible chord found:", format_chord_name(results[0], results[1]))


def main():
    print("Welcome to Chord Finder!")
    user_input = input("Enter notes: ")

    print("Initial notes: "+str(parse_user_input(user_input)))

    sep_input = parse_user_input(user_input)

    i = 0
    for note in sep_input:
        sep_input[i] = normalize_note(note)
        i+=1
    print("Capitalised notes: "+str(sep_input))

    print("Note values: "+str(notes_to_numbers(sep_input)))
    notes = notes_to_numbers(sep_input)
 
    results = find_possible_chords(notes)
    
    print_results(results)

if __name__ == "__main__":
    main()