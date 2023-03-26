def main():
    propmt = check_calculator("Billamount/tiprate: ")

    print(propmt)
    

def tip_calculator(billamount, tiprate):
    tip = billamount * (tiprate / 100)
    return round(tip,2)


def check_calculator(prompt):
    while True:
        bill_amount_str = input(prompt)
        tip_rate_str = input(prompt)
        try:
            bill_amount = float(bill_amount_str)
            tip_rate = float(tip_rate_str)
            if bill_amount > 0 and tip_rate > 0:
                total = bill_amount + tip_calculator(bill_amount, tip_rate)
                return round(total,2)
                
            else:
                return f'Please enter Positive Value'
        except ValueError:
            continue

if __name__ == "__main__":
    main()
