# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

number  = int(input("Enter your number: "))
fact=1
mylist = []
if number > 0:
    for i in range(1, number+1):
        fact *= i
        mylist.append(fact)
    print(mylist)
else:
    print("Your number is incorrect")
