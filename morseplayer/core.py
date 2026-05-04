import numpy as np
import sounddevice as sd
from math import pi
import wave

SAMPLE_RATE = 44100

MORSE_TABLE = {
"A":".-","B":"-...","C":"-.-.","D":"-..","E":".",
"F":"..-.","G":"--.","H":"....","I":"..","J":".---",
"K":"-.-","L":".-..","M":"--","N":"-.","O":"---",
"P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
"U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",
"1":".----","2":"..---","3":"...--","4":"....-","5":".....",
"6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"
}

REVERSE_TABLE = {v:k for k,v in MORSE_TABLE.items()}


def text_to_morse(text):
    result = []
    for ch in text.upper():
        if ch == " ":
            result.append("/")
        elif ch in MORSE_TABLE:
            result.append(MORSE_TABLE[ch])
    return " ".join(result)


def morse_to_text(morse):
    words = morse.split(" / ")
    decoded = []

    for word in words:
        letters = word.split()
        decoded_word = ""
        for l in letters:
            decoded_word += REVERSE_TABLE.get(l,"?")
        decoded.append(decoded_word)

    return " ".join(decoded)


def unit_duration(wpm):
    return 1.2 / wpm


def generate_beep(duration, freq):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    tone = 0.5 * np.sin(2 * pi * freq * t)
    return tone.astype(np.float32)


def build_audio(morse, wpm, freq):
    unit = unit_duration(wpm)
    audio = []

    for symbol in morse:
        if symbol == ".":
            audio.append(generate_beep(unit, freq))
            audio.append(np.zeros(int(SAMPLE_RATE * unit), dtype=np.float32))

        elif symbol == "-":
            audio.append(generate_beep(unit * 3, freq))
            audio.append(np.zeros(int(SAMPLE_RATE * unit), dtype=np.float32))

        elif symbol == " ":
            audio.append(np.zeros(int(SAMPLE_RATE * unit * 3), dtype=np.float32))

        elif symbol == "/":
            audio.append(np.zeros(int(SAMPLE_RATE * unit * 7), dtype=np.float32))

    return np.concatenate(audio)


def play(text, wpm=20, freq=700):
    morse = text_to_morse(text)
    audio = build_audio(morse, wpm, freq)

    sd.play(audio, SAMPLE_RATE)
    sd.wait()


def save(text, filename, wpm=20, freq=700):
    morse = text_to_morse(text)
    audio = build_audio(morse, wpm, freq)

    with wave.open(filename, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(SAMPLE_RATE)
        f.writeframes((audio * 32767).astype(np.int16))
