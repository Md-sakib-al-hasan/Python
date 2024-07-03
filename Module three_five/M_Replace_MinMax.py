arraySize = int(input())
array=list(map(int,input().split()))
found_min=array.index(min(array))
found_max=array.index(max(array))
array[found_min],array[found_max] = array[found_max],array[found_min]
for i in array:
    print(i,end=" ")