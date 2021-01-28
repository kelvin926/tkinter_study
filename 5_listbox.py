from tkinter import *

root = Tk()
root.title("kelvin tkinter") #창 이름
root.geometry("640x480+100+300") #가로 x 세로 + (나타나는) x좌표 + (나타나는) y좌표

listbox = Listbox(root, selectmode="extended", height=0) #extended: 여러개 선택 가능 / single: 하나만 선택 가능 / height = 보이는 높이, 0:리스트가 포함하는 크기만큼 모두 보임
listbox.insert(0, "apple",) #목록에 넣음
listbox.insert(1, "banana")
listbox.insert(2, "mango")
listbox.insert(END, "berry") #END: 맨 뒤에 넣음
listbox.insert(END, "Hello")
listbox.pack()

def btncmd():
    listbox.delete(END) #END: 맨뒤 / 맨 뒤 부터 목록 삭제
    listbox.delete(0) #맨 앞부터 삭제
    
    print("리스트에는", listbox.size(), "개가 있습니다") #목록 안의 아이템 개수
    
    print("1번째부터 3번째까지의 항목: ", listbox.get(0, 2)) #범위내의 존재하는 아이템들
    
    print("선택된 항목: ", listbox.curselection()) #선택된 항목 (위치로 반환됨.)





btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop() #창 닫히지 않게.