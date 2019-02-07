with open('input.txt','r') as f:
    x=f.read().splitlines()

for i in x:

    a,b=i.split(';')
    a=list(map(int,a.split(',')))
    b=list(map(int,b.split(',')))

    if set(a).intersection(set(b)):
        print(*set(a).intersection(set(b)))

    else:
        print('\n')