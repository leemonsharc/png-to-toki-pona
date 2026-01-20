import binascii

toki_pona_wordlist = [
    "li", "e", "mi", "ni",
    "jan", "toki", "pona", "pi",
    "la", "tawa", "lon", "ala",
    "sina", "ona", "mute", "tenpo"
]


def main():
    path = input("enter filename: ")
    with open(path, 'rb') as f:
        png = f.read()
    tohex = binascii.hexlify(png).decode()

main()
