n = int(input())
array=list(map(int,input().split()))
even=all(num%2 ==0 for num in array)
op=0
while even:
    op+=1
    array = [num // 2 for num in array]
    even=all(num%2 ==0 for num in array)
print(op)