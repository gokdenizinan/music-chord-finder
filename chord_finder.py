"""
Music Chord Finder - v2

Goal:
Identify basic chords from note names while providing a cleaner
and more user-friendly command-line experience.

Core chord logic:
- Major chords
- Minor chords
- Diminished chords
- Augmented chords
- Inversions
- Sharp notes only

Improved in v2:
- Cleaner welcome screen
- Clearer input instructions
- Example inputs shown to the user
- Repeated input loop
- Exit commands such as "q" or "quit"
- Help command for valid input format
- Better formatting for chord results
- Better formatting for invalid notes
- Better formatting for no-match cases
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
    if results != None:
        print("Possible chord found:", format_chord_name(results[0], results[1]))
    else:
        print("No matching chord pattern found!")

def print_welcome():
        ascii_art = r"""
                     |\                         __3__          |         
____|\_______________|\\_______________|_______'__|__`___|_____|___|__________
____|/___3_|________@'_\|__|_____|_____|___|___|__|__|___|_|__@'___|___|___|__
___/|____-_|____________|__|_____|____@'___|__@'_@'_@'___|_|______@'___|___|__
__|_/_\__4_|___|_______@'__|____O'_________|____________O'_|__________@'___|__
___\|/_____|___|___________|_______________|_______________|_______________|__
    /         O'                                                  
"""
        print("\nMusic Chord Finder")
        print(ascii_art)
        print("\nEnter notes like: C E G\nType help for instructions.\nType q to quit.\n")
        # If they type help they will be able to see some examples coming from print_examples

def print_examples():
    print("Examples: \nC E G\nE G C\nA C E\nC E G#\n")

def main():
    
    print_welcome()
    user_input = input("Enter notes: ")

    while True:
        if user_input == "q":
            print("Quitting...")
            break
        elif user_input.lower() == "help":
            print_examples()
            user_input = input("Enter notes: ")
        else:
            sep_input = parse_user_input(user_input)

            i = 0
            for note in sep_input:
                sep_input[i] = normalize_note(note)
                i+=1
            flag = True
            for note in sep_input:
                if note not in NOTE_VALUES.keys():
                    print("Invalid set of notes!")
                    flag = False
                    break
            if flag == True:    
                notes = notes_to_numbers(sep_input)

                results = find_possible_chords(notes)
                
                print_results(results)

if __name__ == "__main__":
    main()