q=int(input())
while q!=0:
    val=input()
    val,val1=map(int,val.split())
    if val>val1:
        ten=val
        val=val1
        val1=ten
    sum=0
    for num in range(val+1,val1):
        if(num%2==1):
            sum+=num
    print(sum)
    q-=1

