from tkinter import *

root = Tk()
root.title("kelvin tkinter") #창 이름
root.geometry("640x480+100+300") #가로 x 세로 + (나타나는) x좌표 + (나타나는) y좌표

chkvar = IntVar() #chkvar에 int형으로 값을 저장한다. (1 / 0)
chkbox = Checkbutton(root, text="no more today", variable=chkvar)
chkbox.select() #자동 선택 처리
chkbox.deselect() #선택 해제 처리 (기본 값)
chkbox.pack()

chkvar2 = BooleanVar() #Boolean형으로 값을 저장 (True, False)
chkbox2 = Checkbutton(root, text="no more this week", variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get()) # 0: 체크 해제, 1: 체크
    print(chkvar2.get()) # False, True



btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop() #창 닫히지 않게.