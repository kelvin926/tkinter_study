from tkinter import *

root = Tk()
root.title("kelvin tkinter") #창 이름
root.geometry("640x480+100+300") #가로 x 세로 + (나타나는) x좌표 + (나타나는) y좌표

root.resizable(False, False) #x, y 값 변경 불가 (창 크기 변경 불가)



root.mainloop() #창 닫히지 않게.