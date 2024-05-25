#If the bill was $150.00, split between 5 people, with 12% tip.
total = input("how much the total amount is?\n")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
dollar = (input("how much percentage do you want to give?\n"))
tip = int(total) / 100 * int(dollar)
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇
persons = input("how many people are there?\n")
persons_in_int = int(persons)
tip_in_int = int(tip)
amount = (tip / persons_in_int )
amount_1 = round(amount)
print(f"the amount each person should give is {amount_1}")
