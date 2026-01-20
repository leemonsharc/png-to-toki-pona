import binascii


def pngtohex(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    return binascii.hexlify(content).decode()

def main():
    png = input("enter filename: ")
    print(pngtohex(png))

main()
