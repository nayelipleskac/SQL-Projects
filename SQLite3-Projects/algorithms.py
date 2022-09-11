import random

# nums = [2,4,6,8,10,12,14]
# num_var = random.choice(nums)

# for i in nums:
#     if i == num_var:
#         print('found the number:',i, ' index: ',nums.index(i))
#         break

#     else:
#         print('number not found:',i, ' index:', nums.index(i))

# def factorial(n):
#     if n is 1: #This is the base case
#         return 1  #when this condition holds true tells the program to stop and return all the values in sequential order.
#     return n * factorial(n-1)
# n = int(input("Number? "))
# print(factorial(n))

def fibonacci(n):
    n1, n2 = 0,1
    count = 0
    if n is 1: #This is the base case
        return 0 
    if n <= 0: 
        print('enter positive values')
    while count <= n:
        # print(n1)
        nth = n1+n2
        n1 = n2
        n2 =  nth
        count +=1
    return fibonacci(n) * fibonacci(n-1)
n = int(input('Find the nth number in sequence')) 
print(fibonacci(n)) 


