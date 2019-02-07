result=[]
for i in range(1,100):
    if i%2!=0:
        result.append(i)
print('\n'.join(str(i) for i in result))