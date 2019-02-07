with open('input.txt','r') as f:
   x= f.read().splitlines()
for i in x:
    result=list(set(i.split(',')))
    result.sort()
    print(','.join(i for i in result))