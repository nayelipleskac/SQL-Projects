# snakelist = [0,1,2,3]
# print(snakelist[1:])

# Function returns N largest elements
def Nmaxelements(highScores, N):
    final_list = []
  
    for i in range(0, N): 
        max1 = 0
          
        for j in range(len(highScores)):     
            if highScores[j] > max1:
                max1 = highScores[j];
                  
        highScores.remove(max1);
        final_list.append(max1)
          
    print(final_list)
    print(final_list[0])
    print(final_list[1])
  
# Driver code
highScores = [2, 6, 41, 85, 0, 3, 7, 6, 10]
#list1 would be highScores
  
# Calling the function
Nmaxelements(highScores, 5)
