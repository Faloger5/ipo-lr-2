import cmath #импортируем модуль math
x = float(input()) #просим пользователя ввести х
y = float(input()) #просим пользователя ввести у
z = float(input()) #просим пользователя ввести z
b = cmath.sqrt(10*(pow(x, 1/3)+pow(x, y+2)))*(pow(cmath.asin(z), 2) - abs(x-y)) #вычисляем b
print (b) #выводим на экран b
              
                                        
