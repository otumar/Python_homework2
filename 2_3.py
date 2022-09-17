# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

number = int(input("Enter your number: "))
s = 0
dic = {}
summ = 0
for i in range(1, number+1):
    s = round((1+1/i)**i,3)
    dic[i] = s
    summ += s
print(dic)
print(summ)


