gol={}
for _ in range(int(input())):
    name,number=input().split()
    if name not in gol: gol[name]=int(number)
    else: gol[name]+=int(number)
print(*[f'{name} {gol[name]}' for name in sorted(gol)],sep='\n')