#set 3
#iterative
import random, time
nums = [3,6,13,8,23,21]

nums.sort()
x= random.choice(nums)
min_index = 0  
max_index = len(nums)-1

print('random num: ', x)
time.sleep(2)
print(nums)
# value_mid_index = nums[mid_index]
while True: 
    if max_index < min_index:
        break 

    mid_index = (min_index + max_index) // 2
    if x == nums[mid_index]: 
        print('Number was found', x, 'index: ', mid_index)
        break
    elif x > nums[mid_index]: 
        min_index = mid_index + 1
    elif x < nums[mid_index]:
        max_index = mid_index -1


#recursive
def binarySearch(nums):
    nums.sort()
    x= random.choice(nums)
    min_index = 0  
    max_index = len(nums)-1
    mid_index = (min_index + max_index) // 2

    if max_index < min_index: #base case 1 if x doesn't exist
        return 
    if x == nums[mid_index]: #base case 2 when x is found 
        print('Number was found', x, 'index', mid_index)
        return 

    elif x > nums[mid_index]:
        min_index = mid_index +1
        return binarySearch()
    elif x < nums[mid_index]:
        max_index = mid_index -1
        

nums = [3,6,13,8,23,21]
binarySearch(nums)


