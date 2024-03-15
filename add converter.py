print ["def main():
    x = int(input("Enter a decimal number (0-255): "))
    if x < 0 or x > 255:
        print("Decimal number must be in the range 0-255.")
        return

    powers_of_two = [128, 64, 32, 16, 8, 4, 2, 1]
    y = ''
    for power in powers_of_two:
        if x >= power:
            y += '1'
            x -= power
        else:
            y += '0'

    hex_chars = "0123456789ABCDEF"
    hex_number = ''
    for i in range(0, len(y), 4):
        z = y[i:i+4]
        x = int(z, 2)
        hex_number += hex_chars[x]

    print("Binary:", y)
    print("Hexadecimal:", hex_number)

if __name__ == "__main__":
    main"]
