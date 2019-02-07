from collections import Counter
with open('src.txt', 'r') as f:
    x=f.read().splitlines()

for i in x:
    sublist=list(map(int,i.split()))
    countdict=Counter(sublist)
    for k,v in countdict.items():
        if v==max(countdict.values()):
            print(k,end=' ')
    print('\n')
