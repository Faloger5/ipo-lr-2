number_5 = input("Введите число в восьмиричной системе: ")
d0 = int(number_5[4])*(8**0)
d1 = int(number_5[3])*(8**1)
d2 = int(number_5[2])*(8**2)
d3 = int(number_5[1])*(8**3)
d4 = int(number_5[0])*(8**4)
number_10 = d0+d1+d2+d3+d4
print("Десятичное значение: ", number_10)
