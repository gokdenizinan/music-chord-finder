# Music Chord Finder

A small Python command-line tool that identifies basic chords from note names.

The project is built as a beginner-friendly Python CLI app. The goal is to practice clean function design, user input handling, chord logic, and simple command-line user experience.

## Current Version

Version 1 is complete.

Version 2 is focused on improving the command-line experience without changing the core chord logic too much.

## Current Features

* Major chords
* Minor chords
* Diminished chords
* Augmented chords
* Inversion support
* Sharp notes only
* Invalid note handling
* Simple Python command-line interface

## Version 2 Goals

* Cleaner welcome screen
* Clearer input instructions
* Example inputs before the user types
* Better formatting for successful chord results
* Better formatting for invalid notes
* Better formatting for no-match cases
* Optional repeated input loop
* Optional exit commands such as `q` or `quit`
* Optional help command
* Optional display of supported chord types
* Keep the project simple and beginner-friendly

## Example

Input:

```text
C E G
```

Output:

```text
C major
```

Inversion example:

```text
E G C
```

Possible output:

```text
C major
```

## Supported Notes

This version supports sharp notes only:

```text
C C# D D# E F F# G G# A A# B
```

Flats such as `Bb`, `Eb`, or `Ab` are not supported yet.

## Supported Chord Types

* Major
* Minor
* Diminished
* Augmented

## Not Supported Yet

* Flats
* Seventh chords
* Ninth chords
* Eleventh chords
* Thirteenth chords
* Web interface
* Django version

## How to Run

### Mac

```bash
python3 chord_finder.py
```

### Windows

```bash
python chord_finder.py
```

## Project Roadmap

### v1.0 — Basic Chord Finder

Completed.

* Major chords
* Minor chords
* Diminished chords
* Augmented chords
* Inversions
* Sharp notes only
* Invalid note handling

### v2.0 — Better CLI Experience

In progress.

* Cleaner welcome screen
* Better user instructions
* Repeated input loop
* Exit command
* Help command
* Better result and error formatting

### v3.0 — Flats Support

Planned.

* Add notes such as `Bb`, `Eb`, and `Ab`
* Handle equivalent notes such as `A#` and `Bb`

### v4.0 — Extended Chords

Planned.

* Seventh chords
* Ninth chords
* Eleventh chords
* Possibly thirteenth chords

### Future Version — Web App

Planned for later.

* Turn the project into a simple web app
* Possibly use Django
* Add a user-friendly interface for entering notes and seeing chord results

## Learning Purpose

This project is not only about music theory. It is also a programming practice project focused on:

* Writing clean Python functions
* Separating logic from presentation
* Handling user input
* Designing a simple CLI experience
* Building a project step by step
* Using Git and GitHub for version control
