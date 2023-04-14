# მოთხოვნა: დაწერეთ პროგრამა, რომელიც დაითვლის რამდენი ფუტია ოთახი და ასევე ცალკე გამომიანგარიშეთ რამდენი კვადრატია


## კითხვები:
 - რამდენია ოთახის სიგრძე ?
 - რამდენია ოთახის სიგანე ?
 - კვადრატულობა და ფუტის შედეგი ცალ-ცალკე უნდა იყოს გამოსახული თუ ერთად?
 - რა უნდა გამოჰქონდეს იმ შემთხვევაში თუ რიცხვით მნიშვნელობას მომხმარებელი არ შეიყვანას

 ## ტექნიკური დავალება
 დაწერეთ პროგრამა, რომელშიც იუზერი ცალ-ცალკე შეიყვანს ინფორმაციას ოთახის სიგრძესა და სიგანეს შესახებ, რომლის შედეგად კომპიუტერი ავტომატურად დაითვლის შედეგს და გამოსახავს ცალ-ცალკე ოთახის კვადრატულობასა და ფუტს. იმ შემთხვევაში თუ იუზერის მიერ შეყვანილი ინფორმაცია იქნება არა რიცხვითი პროგრამამ გააგრძელოს მუშაობა იქამდე, სანამ იუზერი სწორ ინფუთს არ შეიყვანს. 


 ### არსებითი სახელი:
  - პროგრამა
  - იუზერი
  - ინფორმაცია
  - ოთახი 
  - სიგრძე
  - სიგანე
  - კომპიუტერი
  - შედეგი
  - კვადრატულობა
  - ფუტი
  - არა რიცხვითი
  - ინფუთი


 ### ზმნა
 - დაწერა
 - შეყვანა
 - დათვლა
 - გამოსახვა
 - გაგრძელება


## Prompts, Process, Output

Inputs: Length of room
Inputs: Width of room
Process: Calculate feet and sqm of room
Output: feet of room, sqm of room


### Testing
Input: "What is the length of room? " = 15
Input: "What is the width of room? " = 20

Process: Input_1 * Input_2 = Feet of room
         Convert feet value to sqm 


Input: "What is the length of room? " = 15 meter
Input: "What is the width of room?   = 2 meter

continue
    result: "Please write only numeric value"


### Pseudo code

length = input("Please Enter the lenfth of room? ")
width = input("Please Enter the width of room? ")

if lenght.isnum() and width.isnum():
    sqf = length * width
    sqm = sqf * 0.09290304 (this is the conversion number )

print(sqf, sqm)

End()