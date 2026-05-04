import argparse
from .core import play, save, text_to_morse, morse_to_text


def main():
    parser = argparse.ArgumentParser(
        prog="morseplayer",
        description="Convert text to Morse code, play it or save as WAV file"
    )

    parser.add_argument(
        "input",
        help="Text to encode OR Morse code to decode"
    )

    parser.add_argument(
        "--decode",
        action="store_true",
        help="Decode Morse code to text instead of encoding"
    )

    parser.add_argument(
        "--wpm",
        type=int,
        default=20,
        help="Speed in words per minute (default: 20)"
    )

    parser.add_argument(
        "--freq",
        type=int,
        default=700,
        help="Tone frequency in Hz (default: 700)"
    )

    parser.add_argument(
        "--save",
        metavar="FILE.wav",
        help="Save output audio to WAV file instead of playing"
    )

    args = parser.parse_args()

    # Decode mode
    if args.decode:
        result = morse_to_text(args.input)
        print(result)
        return

    # Encode mode
    if args.save:
        save(args.input, args.save, wpm=args.wpm, freq=args.freq)
        print(f"[✓] Saved Morse audio to {args.save}")
    else:
        play(args.input, wpm=args.wpm, freq=args.freq)
