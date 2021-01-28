from tkinter import *

root = Tk()
root.title("kelvin tkinter") #창 이름
root.geometry("640x480+100+300") #가로 x 세로 + (나타나는) x좌표 + (나타나는) y좌표

txt = Text(root, width=30, height=5) #여러줄로 입력 받을 때
txt.pack()
txt.insert(END, "글자 입력 ㄲ") #기본 값


e = Entry(root, width=30) #한줄로만 입력 받을 때
e.pack()
e.insert(0, "한줄만!")


def btncmd():
    print(txt.get("1.0", END)) # 텍스트 가져옴 / 1.0: 첫번째 위치부터 가져와라 / 0: 0번째 column 위치에서 가져와라 / text의 경우 1.0, END로.
    print(e.get()) #엔트리 가져옴
    
    txt.delete("1.0", END) #텍스트 삭제
    e.delete(0, END) #엔트리 삭제

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop() #창 닫히지 않게.