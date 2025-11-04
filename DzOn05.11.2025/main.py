import json
def f1():
    print('Нажмите enter если хотите покинуть ввод'+'\n'+'Ввод данных: Имя | Последний вход | Время на сайте')
    users=[]
    with open('js.json','w') as file:
        user=input()
        while user!='':
            name, last_enter, time = user.split()
            users.append({'name': name, 'last_enter': last_enter, 'time': time})
            user = input()
        json.dump(users,file)
def f2():
    with open('js.json', "r") as file:
        pObj = json.load(file)
    for i in pObj:
        print(f'Имя: {i['name']}')
        print(f'Последний вход: {i['last_enter']}')
        print(f'Время на сайте: {i['time']}'+'\n')
while True:
    print('Основное меню:'+'\n'+'Нажмите enter чтобы выйти'+'\n'
          +'Нажмите 1 если хотите ввести данные'+'\n'+'Нажмите 2 если хотите посмотреть данные')
    op=input()
    if op=='':
        break
    elif op=='1':
        f1()
    elif op=='2':
        f2()
    else: print('Неправильный ввод')