def main():
    text = calculate_string_length("Please enter the text: ")
    print(text)

def calculate_string_length(words):
    while True:
        text = input(words)
        try: 
            split_text = text.split(" ")
            join_text = "a".join(split_text)
            if join_text.isalpha():
                length = len(join_text)

                return length
        except:
            continue

if __name__ == '__main__':
    main()


