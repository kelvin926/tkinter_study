from tkinter import *

root = Tk()
root.title("kelvin tkinter") #창 이름
root.geometry("640x480+100+300") #가로 x 세로 + (나타나는) x좌표 + (나타나는) y좌표


Label(root, text="select menu").pack() #변형

burger_var = IntVar() #여기에 int형으로 값을 저장
btn_burger1 = Radiobutton(root, text="hamburger", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="cheezeburger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="chickenburger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


Label(root, text="selet drink").pack()

drink_var = StringVar() #여기에 string형으로 값을 저장
btn_drink1 = Radiobutton(root, text="coke", value="coke", variable=drink_var)
btn_drink2 = Radiobutton(root, text="sider", value="sider", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get()) #선택된 햄버거 라디오 항목의 값 (value) 출력
    print(drink_var.get()) #선택된 음료 라디오 항목의 값 (value) 출력


btn = Button(root, text="order", command=btncmd)
btn.pack()


root.mainloop() #창 닫히지 않게.