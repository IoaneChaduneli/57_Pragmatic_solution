def main():
    first_number = input("1st number: ")
    second_number = input("2nd number: ")
    make_operation = math_operation(first_number, second_number)
    print(make_operation)


def math_operation(x,y):
    
    if x.isnumeric() and y.isnumeric():
        x = int(x)
        y = int(y)
        if x > 0 and  y > 0: 
            plus= x + y 
            subtraction= x - y 
            multiply= x * y 
            division = x / y 
        
        return f'{x} + {y} = {plus}\n{x} - {y} = {subtraction}\n{x} * {y} = {multiply}\n{x} / {y} = {division}'
    
    else:
        return f'It is not possible prompt to be negative or non-numeric value'
            

if __name__ == "__main__":
    main()