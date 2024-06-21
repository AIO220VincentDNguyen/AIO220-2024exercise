#Exercise 3: Viết function tính loss theo regression loss function
import math
import random

def Loss_func():
    num_samples = input('input number of samples: ')
    if not num_samples.isnumeric():
        print('number of samples must be an intger number')
        return
    num_samples = int(num_samples)
    loss_name = input('input loss name:')
    sum = 0
    for i in range(num_samples):
        y = random.uniform(0,10)
        y_hat = random.uniform(0,10)
        if loss_name == 'MAE':
            diff = abs(y - y_hat)
        else:
            diff = (y - y_hat)**2
        sum += diff
    
    print(f'loss name: {loss_name}, sample: {i}, y: {y}, y_hat: {y_hat}, loss: {diff}')

    final_loss = math.sqrt(sum/num_samples) if loss_name == 'RMSE' else sum/num_samples
    print(f'final loss: {final_loss}')
Loss_func()