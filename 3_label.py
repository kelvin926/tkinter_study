from tkinter import *
root = Tk()
root.title("kelvin tkinter") #창 이름

label1 = Label(root, text="hello")
label1.pack()

photo = PhotoImage(file="tkinter_study/check.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="hi") #텍스트 변경
    
    global photo2 #메모리 x
    photo2 = PhotoImage(file="tkinter_study/no.png")
    label2.config(image=photo2) #이미지 변경

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop() #창 닫히지 않게.
