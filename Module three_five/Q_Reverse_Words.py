st=input()
sts=st.split()
for i in sts:
    re=i[::-1]
    if i ==sts[-1]:
        print(re,end="")
    else: 
        print(re,end=" ")
