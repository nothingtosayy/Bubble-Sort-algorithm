#bubble sort algorithm

def bubblesort(list):
    for j in range(len(list)):
        for i in range(len(list)-j-1):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
        
    return list    
        
        
list = list(map(int,input().split()))
print("Sorted List: ",bubblesort(list))
