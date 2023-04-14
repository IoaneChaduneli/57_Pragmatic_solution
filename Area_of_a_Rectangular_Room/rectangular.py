def main():
    attempt = 0
    while attempt < 4:
        length = input("What is the length of room? ")
        width = input("What is the width of room? ")
        if length.isdigit() and width.isdigit():
            sqm = sqf_to_sqm(length, width)
            print(sqm)
            break
        else:
            attempt += 1
            print("Maximum number of attempts exceeded")


def calculate_sqf(length, width):
    return float(length) * float(width)
       

def sqf_to_sqm(length, width):
    sqm = calculate_sqf(length, width) * 0.09290304
    return round(sqm,2)
   


if __name__ == '__main__':
    main()
