import random

def selectsort(array):
    
    arraylen = len(array)

    for itemA in range(arraylen-1):
        
        index = itemA
        
        for itemB in range(itemA+1, arraylen):
            
            if array[index] > array[itemB]:
                
                index = itemB
       
        array[itemA], array[index] = array[index], array[itemA]


array = []

for i in range(6):

    array.append(random.randint(1, 10))

print('Before the array : ', array)
selectsort(array=array)
print('After the array : ', array)
