import random

base = [
     
        {'author': 'Mother Teresa', 'phrase':'Spread love everywhere you go. Let no one ever come to you without leaving happier.'},
        {'author':'Margaret Mead', 'phrase':'Always remember that you are absolutely unique. Just like everyone else. ' },
        {'author':'Eleanor Roosevelt','phrase' :'The future belongs to those who believe in the beauty of their dreams. '},
        {'author':'Benjamin Franklin','phrase' :'Tell me and I forget. Teach me and I remember. Involve me and I learn.'},
        {'author':'Helen Keller', 'phrase':'The best and most beautiful things in the world cannot be seen or even touched — they must be felt with the heart.'},
        {'author':'Aristotle', 'phrase':'It is during our darkest moments that we must focus to see the light'}
    
]

for qoutes in base:
    if not qoutes in base:
        print("Wrong value")

x = random.choice(base)

print(x["author"])