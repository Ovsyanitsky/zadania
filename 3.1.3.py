x = int(input())
sum = 0 #переменная, в которую будет записываться сумма
while (x != 0):
    sum = sum + x % 10
    x = x // 10
print("Сумма цифр числа равна: ", sum)