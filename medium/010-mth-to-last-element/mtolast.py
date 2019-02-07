with open('src.txt','r') as f:
    x=f.read().splitlines()
for i in x:
   sublist=list(i.split())
   indexat=sublist.pop()
   print(sublist[-int(indexat)])
