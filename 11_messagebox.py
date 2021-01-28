from tkinter import *
import tkinter.messagebox as msgbox #messagebox

root = Tk()
root.title("kelvin tkinter") #창 이름
root.geometry("640x480+100+300") #가로 x 세로 + (나타나는) x좌표 + (나타나는) y좌표


#기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료됐습니다.")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진됐습니다.")

def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    response = msgbox.askretrycancel("재시고 / 취소", "재시도 취소")
    print("응답", response) # True, False, None -> 예:1, 아니오0, 그 외
    if response == 1: 
        print("재시도")
    elif response == 0:
        print("취소")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?")
    print("응답", response) # True, False, None -> 예:1, 아니오:0, 그 외
    if response == 1: 
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")


Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()


root.mainloop() #창 닫히지 않게.