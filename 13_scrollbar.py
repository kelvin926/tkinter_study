from tkinter import *

root = Tk()
root.title("kelvin tkinter") #창 이름
root.geometry("640x480+100+300") #가로 x 세로 + (나타나는) x좌표 + (나타나는) y좌표

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set) #set이 없으면 멈추지 않고 바로 위로 올라옴.
for i in range(1, 32):
    listbox.insert(END, str(i) + "일")

listbox.pack(side="left")

scrollbar.config(command=listbox.yview) #상하 이동

root.mainloop() #창 닫히지 않게.