morseplayer

A simple Python tool for converting text to Morse code, decoding Morse back to text, and playing Morse code as audio.

Features
- Convert text to Morse code
- Decode Morse code back to text
- Play Morse code as audio beeps
- Save Morse audio as a WAV file
- Simple command line interface (CLI)

Installation

download the project from github

cd morseplayer 



pip install .

Command Line Usage

Encode text and play Morse audio:

morseplayer "hello world"

Decode Morse code:

morseplayer "... --- ..." --decode

Set speed (words per minute):

morseplayer "hello" --wpm 25

Set tone frequency (Hz):

morseplayer "hello" --freq 600

Save Morse audio to a WAV file:

morseplayer "hello world" --output output.wav

Python API Usage

from morseplayer import text_to_morse
morse = text_to_morse("hello")
print(morse)

from morseplayer import morse_to_text
text = morse_to_text(".... . .-.. .-.. ---")
print(text)

from morseplayer import play
play("hello world", wpm=20, freq=700)

from morseplayer import save
save("hello world", "output.wav", wpm=20, freq=700)

License
MIT License
created by Sobhan Chegini
