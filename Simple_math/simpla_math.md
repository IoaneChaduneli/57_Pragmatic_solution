### მოთხოვნა: ჩავატაროთ მათემათიკური ოპერაციები

## შეკითხვები
1. რა სახის მათემათიკური ოპერაციებს უნდა ითვლიდეს პროგრამა
1. რიცხვები იუზერს უნდა შეყავდეს თუ რაიმე ბაზიდან წამოღებული რიცხვების მათემათიკურ ოპერაციებს უნდა აკეთებდეს
1. რამდენ გამოსახულებიან ოპერაციას უნდა აკეთებდეს პროგრამა
1. პროგრამამ პროცესის დასრულების შემდგომ რა უნდა გამოაჩინოს ეკრანზე


## ტექნიკური დავალება
დაწერეთ პროგრამა, რომელშიც იუზერი შეიყვანს ორ რიცხვს და შედეგად პროგრამა დაგვიბრუნებს ამ ორი რიცხვის ჯამსა,გამრავლებას, პირველი რიცხვის სხვაობას და გაყოფას მეორე რიცხვზე. იმ შემთხვევაში თუ იუზერის სტრინგი არ იქნება სრულიად რიცხვით შემცვლელი დაუბრუნოს ერორი და პროგრამამ მომხმარბელს აცნობოს ამის შესახებ. თუ იუზერის მიერ შეყვანილი ინფორმაცია იქნება ცარიელი, პროგრამა გაჩერდეს და მომხმარებელს დაუბრუნოს ერორი


არსებითი სახელი:
 - პროგრამა
 - იუზერი
 - რიცხვი
 - სტრინგი
 - ერორი
 
ზმნა:
 - დაწერა
 - შეყვანა
 - დაბრუნება
 - ცნობა
 - გაჩერება
 

Inputs, Process, Outputs

Inputs: 'Prompts of the first and second number'
Process: Convert this number to int and calculate the math operation(+ - : /)
Outputs: display the result of math operation(+ - : /)


Testing process

Inputs: 1st number - 10
        2nd number - 5

Expected results: 
        10 + 5 = 15
        10 - 5 = 5
        10 : 5 = 2
        10 / 5 = 2


Inputs: 1st number - w10
        2nd number - 10

Expected results:
    f'The first number is numeric '


Inputs: 1st number - -2
        2nd number - 2

Expeted results:
    f'This program is not friendly with negative number'



## fseudocode - ფსევდო კოდი

 - 1st_num = input("1st number: ")
 - 2nd_num = input("2nd number: ")

Create_list of math operations like = [
    +
    -
    :
    /
]


 - This prompt must be convert to integers like int(1st_num), int(2nd_num)

 - if both number is more than zer0 like both > 0 
      make a loop if we want to use all
      for _ in mathoperation:
          1st _ 2nd 
          print(1st str(_) 2nd, total)


End


