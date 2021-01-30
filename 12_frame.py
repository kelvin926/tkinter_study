from tkinter import *

root = Tk()
root.title("kelvin tkinter") #창 이름
root.geometry("640x480+100+300") #가로 x 세로 + (나타나는) x좌표 + (나타나는) y좌표

Label(root, text="메뉴를 선택해 주세요").pack(side="top") #side:위치

Button(root, text="주문하기").pack(side="bottom")


frame_burger = Frame(root, relief="solid", bd=1) #선으로 된 프레임
frame_burger.pack(side="left", fill="both", expand="True") #좌측 정렬, 꽉 채움, 펼침

Button(frame_burger, text="hamburger").pack()
Button(frame_burger, text="cheezeburger").pack()
Button(frame_burger, text="chickenburger").pack()

frame_drink = LabelFrame(root, text="drink") #제목이 적힌 프레임
frame_drink.pack(side="right", fill="both", expand="True") #우측 정렬, 꽉 채움, 펼침

Button(frame_drink, text="coke").pack()
Button(frame_drink, text="sider").pack()

root.mainloop() #창 닫히지 않게.