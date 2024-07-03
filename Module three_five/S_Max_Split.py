st=input()
count=0
r=0
l=0
stroe_st=[]
for char in st:
    if char=='L':
        l+=1
    else:
        r+=1
    if l ==r :
        count+=1
        stroe_st.append(st[:l+r])
        st=st[l+r:]
        l=0
        r=0
print(count)
for sk in stroe_st:
    print(sk)
        