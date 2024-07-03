n,q=list(map(int,input().split()))
array = list(map(int,input().split()))
array_oneIndex=array[0]
for i in range(1,n):
    array[i]=array[i]+array[i-1]
# print(array)
while q!=0:
    star,end = list(map(int,input().split()))
    if star == 1 :
        print(array[end-1])
    else:
        sk1=array[end-1]
        sk2=array[star-2]
        sum=sk1-sk2
        print(sum)

    q-=1