import tkinter.ttk as ttk #ttk
from tkinter import *

root = Tk()
root.title("kelvin tkinter") #창 이름
root.geometry("640x480+100+300") #가로 x 세로 + (나타나는) x좌표 + (나타나는) y좌표


values = [str(i) + "일" for i in range(1, 32)] #1일 ~ 31일
combobox = ttk.Combobox(root, height=5, value=values)
combobox.pack()
combobox.set("card date") #최초 목록 제목 설정


readonly_combobox = ttk.Combobox(root, height=10, value=values, state="readonly") #readonly = 선택 값 임의 변경 불가능하게. #height = 펼쳤을 때 최대 몇개까지 보이는지.
readonly_combobox.current(0) #0번째 인덱스 값 선택
readonly_combobox.pack()
readonly_combobox.set("card date") #최초 목록 제목 설정


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())


btn = Button(root, text="select", command=btncmd)
btn.pack()


root.mainloop() #창 닫히지 않게.