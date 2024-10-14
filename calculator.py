from tkinter import *

#yazma
def write(x):
    s = len(entry.get())
    entry.insert(s, str(x))

calculation = 0
number1 = 0
number2 = 0

#işlemler
def transactions(x):
    global calculation
    calculation = x
    global number1
    number1 = float(entry.get())
    print(calculation)
    print(number1)
    entry.delete(0, 'end')

#hesaplama
def calculate():
    global number2
    number2 = float(entry.get())
    print(number2)
    global calculation
    result = 0
    if(calculation == 0):
        result = number1 + number2
    elif(calculation == 1):
        result = number1 - number2
    elif (calculation == 2):
        result = number1 * number2
    elif (calculation == 3):
        result = number1 / number2
    entry.delete(0, 'end')
    entry.insert(0, str(result))

def clsButton():
    entry.delete(0, 'end')

def backButton():
    entry.delete(len(entry.get())-1)

def closeButton():
    window.destroy()


window = Tk()
window.geometry("250x300")
window.title("Calculator")

entry = Entry(font="Verdana 14 bold", background="white", fg="black", width=15, justify=RIGHT)
entry.place(x=20, y=1)

buttons = []

clsButton = Button(text="cls", font="Verdana 14 bold", width="2", command=clsButton)
clsButton.place(x=20, y=35)

backButton = Button(text="back", font="Verdana 14 bold", width="4", command=backButton)
backButton.place(x=70,y=35)

closeButton = Button(text="close", font="Verdana 14 bold", width="5", command=closeButton)
closeButton.place(x=140, y=35)

for i in range(1, 10):
    buttons.append(Button(text=str(i), font="Verdana 14 bold", command=lambda x=i:write(x)))

counter = 0

for i in range(0, 3):
    for j in range(0, 3):
        buttons[counter].place(x=20+j*50, y=85+i*50)
        counter += 1

process = []

for i in range(0, 4):
    process.append(Button(font="Verdana 14 bold", width=2, command=lambda x=i:transactions(x)))

process[0]['text'] = "+"
process[1]['text'] = "-"
process[2]['text'] = "*"
process[3]['text'] = "/"

for i in range(0, 4):
    process[i].place(x=170, y=85+50*i)

zeroButton = Button(text="0", font="Verdana 14 bold", command=lambda x=0:write(x))
zeroButton.place(x=20,y=235)

dotButton = Button(text=".", font="Verdana 14 bold", width=2, command=lambda x=".":write(x))
dotButton.place(x=70,y=235)

equalButton = Button(text="=", font="Verdana 14 bold", command=calculate)
equalButton.place(x=120, y=235)

window.mainloop()