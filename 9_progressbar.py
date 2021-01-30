import tkinter.ttk as ttk #ttk
from tkinter import *
import time

root = Tk()
root.title("kelvin tkinter") #창 이름
root.geometry("640x480+100+300") #가로 x 세로 + (나타나는) x좌표 + (나타나는) y좌표


# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") #indeterminate : 왔다 갔다
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") #determinate : 쭉 가고 반복.
# progressbar.start(10) #10ms마다 움직임.
# progressbar.pack()

# def btncmd():
#     progressbar.stop()


# btn = Button(root, text="stop", command=btncmd)
# btn.pack()


p_var2 = DoubleVar() #실수 범위
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(1, 101): #1 ~ 100
        time.sleep(0.01) # 0.01초 대기
        
        p_var2.set(i) #progressbar2의 값 설정
        progressbar2.update() #ui 업데이트
        print(p_var2.get())


btn2 = Button(root, text="start", command=btncmd2)
btn2.pack()


root.mainloop() #창 닫히지 않게.