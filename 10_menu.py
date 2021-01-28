from tkinter import *

root = Tk()
root.title("kelvin tkinter") #창 이름
root.geometry("640x480+100+300") #가로 x 세로 + (나타나는) x좌표 + (나타나는) y좌표

menu = Menu(root)

def create_new_file():
    print("create new file")

#File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New window")
menu_file.add_separator() #구분
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") #비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) #나감
menu.add_cascade(label="File", menu=menu_file)

#Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")

#Language 메뉴 추가 (radio 버튼을 통해서 택 1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

#View 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop() #창 닫히지 않게.