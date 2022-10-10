

#exercise 1- linear search
# setup_code= 'from math import factorial'

import time, timeit
start = time.time()
setup = '''
import random

nums = [2,4,6,8,10,12,14]
num_var = random.choice(nums)

def linearSearch(nums):
    for i in nums:
        if i == num_var:
            print('found the number:',i, ' index: ',nums.index(i))
            break
        else:
            print('number not found:',i, ' index:', nums.index(i))
'''
# start_time = timeit.default_timer()
# print('the starttime is, ', start_time)
# end = time.time()
print('The time of execution of the linear search using time.time is: ', (end - start), 'ms') #0.0023 ms
print(f"The time of execution of the linear search using timeit is:  {timeit.timeit(setup= setup, stmt = 'linearSearch', number = 1000000)}") # ms
# print('The time difference is : ', timeit.default_timer() - start_time)



# def factorial(n):
#     if n is 1: #This is the base case
#         return 1  #when this condition holds true tells the program to stop and return all the values in sequential order.
#     return n * factorial(n-1)
# n = int(input("Number? "))
# print(factorial(n))

#exercise 2
# def fibonacci(n):
#     if n ==0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# n = int(input('Find the nth number in fibonacci sequence: ')) 
# #print just n
# print(fibonacci(n)) 
# #to print out sequence of n
# for i in range(n):
#     print(fibonacci(i))

#exercise 3
# print(123%10+(123//10))

#adding the sum of entered digits

# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n%10+sum(n//10)

# n = int(input('Enter a number: '))
# print('sum: ', sum(n))


#exercise 4
# print('hello'[1:])
# def reverse(x):
#     if len(x) == 0:
#         return x 
#     else:
#         return reverse(x[1:]) + x[0]

# x = input('Enter a string: ')
# print(reverse(x))

#exercise 5- pascal's triangle without recursion
# print(1)
# layer = [1, 1]
# layers = 1
# while layers < 10:
#     for elem in layer:
#         print(elem,end=' ')
#     print()
#     new_layer = []
#     for i in range(len(layer)-1):
#         num1 = layer[i]
#         num2 = layer[i+1]
#         new_layer.append(num1 + num2)
#     new_layer=[1] + new_layer + [1]
#     layer=new_layer
#     layers+=1

#with recursion

# def pascal(layer): 
#     # layer = [1,1]
#     # print('layers: ', layers)
#     if len(layer) > 10:  #base cases
#         return
#     # if layers == 1:
#     #     return [[1]]   
#     else: 
#         for i in layer:
#             print(i, end = ' ')
#         print()
#         #recursive call :
#         # rec_row = pascal(layer-1)
#         # prev_layer= rec_row[-1]
#         new_layer = []
#         for i in range(len(layer)-1):
#             num1= layer[i]
#             num2 = layer[i+1]
#             new_layer.append(num1 + num2)

#         new_layer = [1] + new_layer + [1] 
#         layer = new_layer
#         # rec_row.append(new_layer)     
#         pascal(layer)
        
# print(1)
# layer = [1,1]
# pascal(layer)





