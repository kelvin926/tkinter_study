'''
1. title : 제목 없음 - 메모장 - ㅇ
2. 메뉴 : 파일, 편집, 서식, 보기, 도움말 - ㅇ
3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만. - ㅇ
3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기.
3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기.
3-3. 끝내기 : 프로그램 종료 - ㅇ
4. 프로그램 시작 시 본문은 비어있는 상태 - ㅇ
5. 하단 status 바는 필요 없음 - ㅇ
6. 프로그램 크기, 위치는 자유롭게, but 크기 조절 가능해야 함. - ㅇ
7. 본문 우측에 상하 스크롤 바 넣기. - ㅇ
'''
import os
from tkinter import *


root=Tk()

root.title("제목 없음 - 메모장")

root.geometry("300x300")
root.resizable(True,True)

menu = Menu(root)

filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): #파일 있으면 True
        with open(filename, "r", encoding="utf-8") as file:
            txt.delete("1.0", END) #텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) #파일 내용을 본문에 입력
    

def save_file():
    with open(filename, "w", encoding="utf-8") as file: #텍스트 위젯 본문을 가져와서 저장.
        file.write(txt.get("1.0", END))



file_menu=Menu(menu, tearoff=0)
file_menu.add_command(label="새 파일")
file_menu.add_separator()
file_menu.add_command(label="열기", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="저장", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="끝내기", command=root.quit)

menu.add_cascade(label="파일", menu=file_menu)


# 부가 메뉴
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")


# 본문
txt =Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)


root.config(menu=menu)

root.mainloop()