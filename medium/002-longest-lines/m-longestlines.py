with open('src.txt', 'r') as f:
    x=f.read().splitlines()

outputlines=x.pop(0)
result=sorted(x,key=len,reverse=True)
print('\n'.join(i for i in result[:int(outputlines)]))