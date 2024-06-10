#Excercise 4: Viết Functions ước lượng các hàm số sin(x), cos(x), sinh(x), cosh(x)
import math

def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x-1)
def approx_sin(x, n):
    result = 0
    for i in range(n):
        result = result + math.pow(-1, i) * math.pow(x, 2*i+1) / factorial(2*i+1)
    return result

def approx_cos(x, n):
    result = 0
    for i in range(n):
        result = result + math.pow(-1, i) * math.pow(x, 2*i) / factorial(2*i)
    return result

def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result = result + math.pow(x, 2*i+1) / factorial(2*i+1)
    return result

def approx_cosh(x, n):
    result = 0
    for i in range(n):
        result = result + math.pow(x, 2*i) / factorial(2*i)
    return result

print(approx_sin(3.14, 10))
print(approx_cos(3.14, 10))
print(approx_sinh(3.14, 10))
print(approx_cosh(3.14, 10))