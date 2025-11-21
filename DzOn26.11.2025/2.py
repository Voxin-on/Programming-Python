import json
import tkinter as tk

def clickButton(x,vars):
    global count,curQ
    result=[i for i, var in enumerate(vars, 1) if var.get()]
    if set(result)==set(x):
        count+=1
    curQ += 1
    for i in baseWindow.winfo_children():
        i.destroy()
    if curQ<=len(questions):
        showQuestion(curQ)
    else: showResult()

def showQuestion(cur):
    i=questions[str(cur)]
    label = tk.Label(baseWindow,
                      text=i['question'],
                      fg="black",
                      font=("Arial", 18))
    label.pack()


    vars = []
    for j, variant in enumerate(i['variants'], 1):
        var = tk.IntVar()
        vars.append(var)
        tk.Checkbutton(baseWindow, text=variant, variable=var).pack()


    button = tk.Button(baseWindow,
                        text="Ответить",
                        font=("Arial", 18),
                        command=lambda: clickButton(i['right'],vars))
    button.pack()

def showResult():
    labelRes = tk.Label(baseWindow,
                        text=f"Кол-во правильных ответов {count} из {len(questions)}\n"
                             f"Процент правильных ответов {count / len(questions)*100:.1f}%",
                        fg="black",
                        font=("Arial", 18))
    labelRes.pack()



baseWindow = tk.Tk()
baseWindow.title("The test system")
baseWindow.geometry("1200x800")


nameJs='questions.json'
with open(nameJs, 'r',encoding='utf-8') as f:
    questions=json.load(f)

count=0
curQ=1
showQuestion(curQ)

baseWindow.mainloop()