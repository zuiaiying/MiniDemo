#QuickSort

def quicksort(l,low,high):
    i = low
    j = high
    if i >= j:
        return l
    key = l[i]
    while i < j:
        while i < j and l[j] >= key:
            j = j-1
        l[i] = l[j]
        while i < j and l[i] <= key:
            i = i+1
        l[j] = l[i]
    l[i] = key
    quicksort(l,low,i-1)
    quicksort(l,j+1,high)

l = [1,2,3,2,2,4,5,7,9,5,3,2]
quicksort(l,0,len(l)-1)
print(l)


