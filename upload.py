import binascii


hex_to_toki = {
    "0": "li", "1": "e", "2": "mi", "3": "ni",
    "4": "jan", "5": "toki", "6": "pona", "7": "pi",
    "8": "la", "9": "tawa", "a": "lon", "b": "ala",
    "c": "sina", "d": "ona", "e": "mute", "f": "tenpo"
}

output = ""

def main():
    path = input("enter png filename without .png: ")
    with open(path + ".png", 'rb') as f:
        png = f.read()
    tohex = binascii.hexlify(png).decode()
    for letter in tohex:
        global output
        totoki = hex_to_toki[letter]
        output += (totoki + " ")
    with open(path + ".tok", "w") as f:
        f.write(output)

main()
