import datetime

def main():
    age = input("Your age: ")
    retire = input("Retire age: ")
    result = calculate_retire_year(age,retire)
    print(result)


def calculate_retire_year(your_age, retire_age):
    if your_age.isnumeric() and retire_age.isnumeric():
        your_age = int(your_age)
        retire_age = int(retire_age)
        after_year = retire_age - your_age
        Current_year = datetime.datetime.now().year
        Retire_year = Current_year + after_year
        if your_age < retire_age:
            return f"You will retire after {after_year} years later\nYou will retire in {Retire_year}"
        else:
            return f"You retired {abs(after_year)} years ago\nYou retired in {Retire_year}"
    else:
        return f"Please write numeric value"
        



if __name__ == "__main__":
    main()