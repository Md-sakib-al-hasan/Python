sk={'tomato':4,'spice':5}
uk={'tomato':5,'curry':5}
for key,value in sk.items():
        for ke,va in uk.items():
            if(key == ke):
                sk[key]=sk[key]+va
                uk[ke]=0

            

print(uk)