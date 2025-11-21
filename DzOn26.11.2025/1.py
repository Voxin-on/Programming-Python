import tkinter as tk

def clickButton():
    result=[question1.get(),question2.get(),question3.get(),question4.get()]
    check=[0]*4
    for j in result:
        if 1<=j<=4:
            check[j-1]+=1
    label5.configure(text=f"Твой результат:\n1 — Адреналин: {check[0]*25}%\n2 — История: {check[1]*25}%\n"
                          f"3 — Разум: {check[2]*25}%\n4 — Общение: {check[3]*25}%")
    with open("result1.txt","w") as f:
        f.write(f"Твой результат:\n1 — Адреналин: {check[0]*25}%\n2 — История: {check[1]*25}%\n"
                          f"3 — Разум: {check[2]*25}%\n4 — Общение: {check[3]*25}%")

baseWindow = tk.Tk()
baseWindow.title("CheckYourGamePersonality")
baseWindow.geometry("1200x800")

question1=tk.IntVar(value=1)
question2=tk.IntVar(value=1)
question3=tk.IntVar(value=1)
question4=tk.IntVar(value=1)

label1 = tk.Label(baseWindow,
                  text="1. Что тебе больше нравится делать в игре?",
                  fg="black",
                  font=("Arial", 18))
label1.pack()
radButton1 = tk.Radiobutton(baseWindow,
                           text="1) Стрелять, бегать, взрывать — всё быстро и громко!",
                           variable=question1,
                           value=1)
radButton1.pack()
radButton1 = tk.Radiobutton(baseWindow,
                           text="2) Исследовать мир, узнавать историю, расти как персонаж",
                           variable=question1,
                           value=2)
radButton1.pack()
radButton1 = tk.Radiobutton(baseWindow,
                           text="3) Думать, решать загадки, планировать ходы",
                           variable=question1,
                           value=3)
radButton1.pack()
radButton1 = tk.Radiobutton(baseWindow,
                           text="4) Играть с друзьями — вместе веселее!",
                           variable=question1,
                           value=4)
radButton1.pack()

label2 = tk.Label(baseWindow,
                  text="2. Какой формат тебе комфортен?",
                  fg="black",
                  font=("Arial", 18))
label2.pack()
radButton2 = tk.Radiobutton(baseWindow,
                           text="1) Короткие сессии — 10–30 минут",
                           variable=question2,
                           value=1)
radButton2.pack()
radButton2 = tk.Radiobutton(baseWindow,
                           text="2) Длинные сессии — погрузиться на час+",
                           variable=question2,
                           value=2)
radButton2.pack()
radButton2 = tk.Radiobutton(baseWindow,
                           text="3) Неважно — главное, чтобы было интересно решать",
                           variable=question2,
                           value=3)
radButton2.pack()
radButton2 = tk.Radiobutton(baseWindow,
                           text="4) Когда соберутся друзья — хоть на ночь!",
                           variable=question2,
                           value=4)
radButton2.pack()

label3 = tk.Label(baseWindow,
                  text="3. Какой жанр тебе ближе?",
                  fg="black",
                  font=("Arial", 18))
label3.pack()
radButton3 = tk.Radiobutton(baseWindow,
                           text="1) Экшн, аркада, гонки",
                           variable=question3,
                           value=1)
radButton3.pack()
radButton3 = tk.Radiobutton(baseWindow,
                           text="2) RPG, приключения, квесты",
                           variable=question3,
                           value=2)
radButton3.pack()
radButton3 = tk.Radiobutton(baseWindow,
                           text="3) Головоломки, стратегии, симуляторы",
                           variable=question3,
                           value=3)
radButton3.pack()
radButton3 = tk.Radiobutton(baseWindow,
                           text="4) Мультиплеер, кооп, онлайн-игры",
                           variable=question3,
                           value=4)
radButton3.pack()

label4 = tk.Label(baseWindow,
                  text="4. Что для тебя главное в игре?",
                  fg="black",
                  font=("Arial", 18))
label4.pack()
radButton4 = tk.Radiobutton(baseWindow,
                           text="1) Экшн, аркада, гонки",
                           variable=question4,
                           value=1)
radButton4.pack()
radButton4 = tk.Radiobutton(baseWindow,
                           text="2) Эмоции и сюжет",
                           variable=question4,
                           value=2)
radButton4.pack()
radButton4 = tk.Radiobutton(baseWindow,
                           text="3) Умственный вызов",
                           variable=question4,
                           value=3)
radButton4.pack()
radButton4 = tk.Radiobutton(baseWindow,
                           text="4) Общение и совместные эмоции",
                           variable=question4,
                           value=4)
radButton4.pack()


button = tk.Button(baseWindow,
                    text="Получить результат",
                    font=("Arial", 18),
                    command=clickButton)
button.pack()
label5 = tk.Label(baseWindow,
                  text="",
                  fg="black",
                  font=("Arial", 18))
label5.pack()

baseWindow.mainloop()