# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = input("Enter a real number: ")
mysum = 0
for i in number:
    if i.isdigit():
        mysum = mysum + float(i)
print(f"The sum of the digits of your number is {mysum}")
