def main():
    item = 1
    subtotal = 0
    while True:
        price = input(f'Enter the price of item {item}: ')
        if price == 'exit':
            break
        else:
            quantity = input(f'Enter the quantity of item {item}: ')
            item += 1
            full_price = calculate_subtotal(price, quantity)
            subtotal += full_price
            tax = round(subtotal * 0.05,2)
            total = subtotal + tax
    print(f'Subtotal: ${subtotal}')
    print(f'Tax: ${tax}')
    print(f'Total: ${total}')
            



def calculate_subtotal(price, quantity):
    try:
        subtotal = float(price) * int(quantity)
        return subtotal
    except ValueError:
        raise ValueError("The value of price is float and value of quantity is integer. Please act what this message alert you.")


if __name__ == '__main__':
    main()
