import cmath 
x = float(input())
y = float(input())
z = float(input())
b = cmath.sqrt(10*(pow(x, 1/3)+pow(x, y+2)))*(pow(cmath.asin(z), 2) - abs(x-y))
print (b)
              
                                        
