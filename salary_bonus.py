#program to get salary bonus of a user

salary=int(input("Enter your salary: ")
)
years=int(input("Enter your years of service: "))

if years>10:

  bonus = salary*0.1

  print(bonus)

if years>=6 and years<=10:

  bonus = salary*0.08

  print(bonus)

if years<6:

    bonus = salary*0.05

    print(bonus)