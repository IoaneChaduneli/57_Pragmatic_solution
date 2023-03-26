# მოთხოვნა: პროგრამამ დათვალოს რამდენი წელი დაგვრჩა პენსიამდე

## კითხვები 
1. რამდენი წლის არის იუზერი?
1. რამდენია საპენსიო ასაკი?
1. რა უნდა შევეკითხოთ პროგრამას?
1. რა უნდა გამოჩნდეს აუთფუთად ეკრანზე?


## ტექნიკური დავალება
დაწერეთ პროგრამა, სადაც იუზერი შეიყვანს ინფორმაციას საკუთარი ასაკისა და პენსიაში გასასვლელი ასაკის წლოვანებას. შედეგად პროგრამა დაითვლის რამდენი წელი დარჩა ამა თუ იმ მომხმარებბელს საპენსიო ასაკამდე და გამოთვლის საპენსიო ასაკი რომელი წელს მოუწევს. აუცილებელია რიცხვითი მნიშვნელობა შეიყვანოს იუზერმა, წინააღმდეგ შემთხვევაში შეატყობინეთ, რომ აუცილებელია იყოს რიცხვითი მნიშვნელობა. თუ მომხმარებელი უკვე პენსიაშია დაგვიბრუნოს უარყოფითი მნიშვნელობა


## Inputs, Procecc and Output

არსებითი სახელები:
 - პროგრამა
 - იუზერი
 - ინფორმაცია
 - ასაკი
 - პენსია
 - წელი
 - მომხმარებელი
 - მნიშვნელობა


 ზმნა: 
 - დაწერა
 - შეყვანა
 - დათვლა
 - დაბრუნება


 Inputs: Prompt Your age
         Prompt Your retire age

Process: Calculate the distinction between them
Outputs: How many years left to retiremnt age and what is the user year of retirement


## Test cases

Inputs: "What is you age": 25
        "What is retirment age": 65

Expected Result: 
                You have left 40 year untill retirement
                You will retire in 20 2063 years

Inputs: "What is you age": 70
        "What is retirment age": 65

Expected Result: 
                You  retired 5 years ago 
                You retired in 2018 years


Inputs: "What is you age": yrt5
        "What is retirment age": 65

Expected Result: 
                Please enter your age



## Pseudocode  - ფსევდო კოდი
- input "What is your age"
- input " What is retire_age"

- Now i want to make a validation of non_numeric character

- if input of age is numeric and input of retire_age is numeric
     retire_age  - your age 
     today year + distinction
    - Also i call Datetime modeul to have dynamic year 
results: 
        You have left distinction year for retirement
        You will retire in sum years. 
 - if age < 0
   - retire age - your age
   - today year + your age
 result:
   - you retired distinction years ago
   - you retired in distinction years.
