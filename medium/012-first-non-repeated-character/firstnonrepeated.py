from collections import Counter
x=input()
result=[]
countchar=Counter(x)
for k,v in countchar.items():
    if v==min(countchar.values()):
        result.append(k)
print(result[0])