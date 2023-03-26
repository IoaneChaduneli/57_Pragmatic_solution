### მოთხოვნა : დამიწერე პროგრამა, რომელიც გამომითვლის ჩაის და         შემდეგ ავტომატურად დამითვლის ჯამურ ღირებულებას.

## შეკითხვები
1. ჩეკის ოდენობა
1. ჩაის პროცენტი
1. რა უნდა შევეკითხოთ იუზერს?
1. რა უნდა გამოჩნდეს ეკრანზე პროგრამის ჩართვისას?
1. რა შედეგი უნდა მოგვცეს პროგრამამ? 


## ტექნიკური დავალება
შექმენის თიფის დათვლის კალკულატორი. იუზერი შეიყვანს ინფორმაციას ჩეკის რაოდენობის და თიფის პროცენტის შესახებ, შედეგად პროგრამა დაითვლის თიფს თანხმებში და ეკრანზე გამოიტანს გადასახდელი თანხის სრულ ოდენობას. 
იმ შემთხვევაში თუ იუზერმა არ შეიყვანა რიცხვი, მაშინ დისფლეიზე არაფერი გამოჩნდეს და გააგრძელოს მუშაობა. როდესაც პროგრამაში შეყვანილი ინფორმაცია იქნება სწორი, მონაცემების საფუძველზე დაითვალოს და პროგრამამ შეწყბიტოს მუშაობა. შევზღუდოთ უარყოფითი რიცხვების შეყვანა პროგრამაში. 


### Inputs, Processes, Outputs
არებითი სახელები:
- ჩეკის რაოდენობა
- თიფის პროცენტი
- თიფი
- სრული ოდენობა
- რიცხვი
- მუშაობა
- ინფორმაცია
- მონაცემები


ზმნები:
- დათვლა
- შეყვანა
- გამოტანა
- შეწყვეტა
- გაგრძელება

Inputs: bill amount, tip rate
Process: calculate
Outputs: tip amount, total amount

## ტესტის გეგმა
inputs:
 - bill amount: 11.25
 - tip rate: 15
 Excpeted results:
  - tip: 1.69
  - total: 12.94

inputs:
 - bill amount: abc1
 - tip rate: 10
 Expected results:
 - Nothing Appear, Program will continue its work Untill it will not get the correct value


inputs:
 - bill amount: tyr
 - tip rate: */er
Expected results:
 - Nothing Appear, Program will continue its work Untill it will not get the correct value

## ფსევდოკოდი - Pseudocode
    initialize billamount  to 0
    initialize tip to 0 
    initialize tip rate to 0
    initialize total amount to 0 

    Prompt Billamount with?
'What is the bill amount? '
    Promt Tiprate with?
'What is tiprate? '

   convert Billamount to number
   Convert tip rate to number

   If Billamount or Tiprate is digit
        tip = billamount * (tip rate / 100)

        round Tip up to nearest cent (2 decimal number)

        total = tip + Billamount 

        Display: Tip: "$", tip
        Display: Total: "$", total
    If Billamount or Tiprate is not Digit 
        Continue its work

    If Billamount or Tiprate is negative values
        Error

End