#Excercise 2: Viết function tính kết quả theo các activation function
import math

x  = input('input x = ')
namefunc = input('name function: ')
# tạo các calc function
def sigmoid(x):
    return 1/(1 + math.e**(-x))

def relu(x):
    if(x <= 0):
        return 0
    return x

def elu(x):
    if(x > 0):
        return x
    return 0.01 * (math.e**x - 1)
def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
#tạo activation function nhận giá trị từ input
def activation_function(x, namefunc):
    if is_number(x) == False:
        print('x must be a number')
        return
    # chuyển x thành số thực, kiểm tra namefunc có phù hợp
    x = float(x)
    if namefunc != 'sigmoid' and namefunc != 'relu' and namefunc != 'elu':
        print(f'{namefunc} is not support')
        return
    # thực hiện tính toán nếu namefunc phù hợp
    elif namefunc == 'sigmoid':
        print(f"sigmoid({x}) = {sigmoid(float(x))}")
    elif namefunc == 'relu':
        print(f"relu({x}) = {relu(float(x))}")
    elif namefunc == 'elu':
        alpha = 0.01
        print(f"elu({x}) = {elu(float(x))}")

activation_function(x, namefunc)