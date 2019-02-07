with open('src.txt','r') as f:
    x=f.read().splitlines()
    print(sum(map(int,x)))
