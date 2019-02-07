x,y,z=map(int,input().split())
def fizzbuzz(x,y,z):
    result=[]
    for i in range(1,z+1):
        if i%x == 0 and i%y == 0:
            result.append('FB')
        elif i%y==0 :
            result.append('B')
        elif i%x==0:
            result.append('F')
        else:
            result.append(i)
    return ' '.join(str(i) for i in result)

print(fizzbuzz(x,y,z))
