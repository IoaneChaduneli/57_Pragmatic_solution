### მოთხოვნა: დაითვალეთ სტრინგების ასოების რაოდენობა და გამოაჩინეთ ეკრანზე

## შეკითხვები
1. რამდენია სტრინგის სიგრძე?
1. რა უნდა შეიყვანოს იუზერმა?
1. რა გვინდა რომ შევეკითხოთ იუზერს
1. თუ სტრინგი არ არის მაშინ რა გვინდა რომ გამოჩნდეს?
1. სწორად გადაცემული მნიშვნელობის შემთხვევაში რა გვინდა რომ გამოჩნდეს?

## ტექნიკური დავალება
შექმენით პროგრამა, რომელიც დაითვლის სტრინგის სიგრძეს და გამოგვიტანს ეკრანზე მის რაოდენას. იმ შემთხვევაში თუ იუზერის მიერ შეყვანილი ინფორმაცია არ არის ასოები, მაშინ პროგრამა გააგრძელოს მუშაობა, მანამდე სანამ იუზერი პროგრამას არ გადასცემს სწორ მნიშვნელობას. 


### Inputs, Process, Outputs

არსებითი სახელები:
 - პროგრამა
 - სტრინგი
 - რაოდენობა
 - იუზერი
 - ასოები
 - მუშაობა
 - მნიშნელობა


ზმნები: 
 - შექმნა
 - დათვლა
 - გამოტანა
 - შეყვანა
 - გაგრძელება
 - გადაცემა



Inputs: enter string 
Process: calculate the string length
Outputs: display the lenght of string


## ტესტის გეგმა

Inputs: 'Hello World'
Expected result: 11

Inputs: '54876503'
Expected result: ''

## Pseudocode - ფსევდოკოდი 

Make a validation - if input is not isalpha() the program continue its work
For example: 
    {
        input: 'hello 4563'
        Ask the user again
    }

Correct Version:
    {
        input: 'Hello World'
        len(input) 
        Display : len of the input is: 
    }

End

