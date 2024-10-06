def f(x):  #повертає значення функції в цій точці
    return x**2 - 2*x - 10

def bisection_method(a, b, tol):
    if f(a) * f(b) >= 0: #Перевірка, чи значення функції на кінцях інтервалу мають різні знаки
        print("Метод половинного ділення не може бути застосований")
        return None
    else:
        while (b - a) / 2 > tol:
            midpoint = (a + b) / 2 # середня точка інтервалу
            if f(midpoint) == 0:
                return midpoint  
            elif f(a) * f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        return (a + b) / 2

# Задання початкових значень 
a = 2
b = 5
tol = 10**-4

# Виклик функції
root = bisection_method(a, b, tol)
print("значення кореня:", root)
