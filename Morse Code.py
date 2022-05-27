import playsound
import time

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ' : '/'}

message = "Morse Code test"
message = " ".join(MORSE_CODE_DICT[c] for c in message.upper())


def play_morse_code(message):
    for c in message:
        if c == ".":
            playsound("short.mp3")
            time.sleep(0.3)
        elif c == ",":
            playsound("long.mp3")
            time.sleep(0.3)
        elif c == "/" or c == " ":
            time.sleep(0.5)
        else:
            print("Invalid Charater")

print(message)
play_morse_code(message)

