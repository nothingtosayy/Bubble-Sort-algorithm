def bubblesort(sequence):
    for i in range(len(sequence)):
        for j in range(0, len(sequence)-1):
            if sequence[j] >= sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
            else:
                 sequence[j], sequence[j+1] = sequence[j], sequence[j+1]
                
    return sequence
    
print(bubblesort(sequence=[5,2,3,4,6,1,3,2,6,5,4,7,6,9,8,8,3,9]))
