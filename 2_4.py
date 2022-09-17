# Задать список из N элементов, заполненных числами из[-N, N]. Найти произведение элементов
# на указанных позициях. 
# Позиции хранятся в списке positions - создайте этот список.
# Например:positions=[1, 3, 6]

number = int(input("Enter your number: "))
p = "1,3,6"
c = 1
mylist = []
for i in range(-number,number+1):
    mylist.append(i)
print(mylist)
mylist1 = p.split(",")
for i in  mylist1:
    print(mylist[int(i.strip())])
    c *= mylist[int(i.strip())]
print(c)
