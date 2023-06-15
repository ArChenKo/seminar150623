# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

bilet = input("Введите 6-ти значный номер проездного билета: ")
a = 0
b = 0
for i in bilet[:3]:
    a += int(i)
for i in bilet[3:]:
    b += int(i)
if a == b:
    print("У Вас счастливый билет! Поздравляем!")
else:
    print("К сожалению Вам не повезло. Но ничего, в следующий раз точно повезет!)")
