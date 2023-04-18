import math, sys

def main():
    length = input("What is the length of room? ")
    width = input("What is the width of room? ")
    ballon = ballon_neccassity(length, width)
    print(ballon)


def sqf_to_sqm(sqf):
    sqm = sqf * 0.09290304
    return sqm

def room_sqm(length, width):
    sqm = sqf_to_sqm(length) * sqf_to_sqm(width)
    return sqm

def ballon_neccassity(length, width):
    try:
        length = int(length)
        width = int(width)
    except ValueError:
        raise ValueError("Please enter numeric value")
    sqm = round(room_sqm(length,width))
    ballon = math.ceil(sqm / sqf_to_sqm(350))
    if ballon < 1:
        ballon = 1
    return f'You will need to purchase {ballon} gallons of paint to cover {sqm} sqare meter'
                                    


if __name__ == '__main__':
    main()


 