from tkinter import *

root = Tk()
root.title("kelvin tkinter") #창 이름

btn1 = Button(root, text="버튼1")
btn1.pack() #버튼 적용

btn2 = Button(root, padx=5, pady=10, text="버튼2") #글씨 여백 확보 (유동적)
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3") #글씨 여백 확보 (유동적)
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") #버튼 크기 자체 설정 (고정적)
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") #fg=폰트색상, bg=바탕색상
btn5.pack()

photo = PhotoImage(file="tkinter_study/check.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("clicked!")

btn7 = Button(root, text="동작O", command=btncmd)
btn7.pack()


root.mainloop() #창 닫히지 않게.
