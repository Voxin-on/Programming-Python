with open('roles.txt', "r",encoding='utf-8') as file:
    file.readline()
    roles={}
    line = file.readline().strip()
    while line!='textLines:':
        roles[line]=[]
        line = file.readline().strip()
    current_role=''
    count=1
    line = file.readline().strip()
    while line:
        if ':' in line:
            role,worlds=line.split(':', 1)
            if role in roles.keys():
                current_role=role
                roles[current_role].append(f'{count}) {worlds.strip()}\n')
                count += 1
            else:
                roles[current_role][-1] += " " + line+'\n'
        else:
            roles[current_role][-1] += " " + line+'\n'
        line = file.readline().strip()
with open('roles.txt', "a",encoding='utf-8') as file:
    file.write('\n\n')
    for role, worlds in roles.items():
        file.write(f'{role}:\n')
        for world in worlds:
            file.write(f'{world}')
        file.write('\n')