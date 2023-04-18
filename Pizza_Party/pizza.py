import math,sys

def main():
    people = get_int_input('How many people? ')
    pizza = get_int_input('How many pizzas do you want? ')
    pieces_needed = calculate_pizza(people, pizza)
    print(pieces_needed)

def calculate_pizza(people, pizza):
    pizza_per_piece = 8
    pizza_pieces = math.ceil((pizza * pizza_per_piece) / people)
    return f'Each person gets {pizza_pieces} pieces of pizza'


def get_int_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Please enter a numeric value")


if __name__ == '__main__':
    main()