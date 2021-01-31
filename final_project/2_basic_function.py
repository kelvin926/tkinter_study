from tkinter import * # __all__
import tkinter.ttk as ttk
from tkinter import filedialog #filedialog는 서브 모듈이기 때문에 *로 넣어지지 않음.
import tkinter.messagebox as msgbox
root = Tk()
root.title("kelvin tkinter") #창 이름
root.resizable(False, False) #x, y 값 변경 불가 (창 크기 변경 불가)


#파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")), initialdir="C:/")
    
    #사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)

#선택 삭제
def del_file():
    for index in reversed(list_file.curselection()): #거꾸로 반환 -> 뒤에서 지워나감 : 앞의 순서를 바뀌지 않게 하기 위해. (reverse를 하면 실제 값에 영향 미침, reversed를 하면 영향 X)
        list_file.delete(index)

#저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == "": #사용자가 취소를 누를 때
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

#시작
def start():
    #각 옵션들 값을 확인
    print("가로 넓이: ", cmb_width.get())
    print("간격: ", cmb_space.get())
    print("포맷: ", cmb_format.get())

    #파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return
    
    #저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return





# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) #x방향(가로)으로 쫙 펼침. , 간격 띄우기

btn_add_file = Button(file_frame, text="파일 추가", padx=5, pady=5, width=12, command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="선택 삭제", padx=5, pady=5, width=12, command=del_file)
btn_del_file.pack(side="right")


# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar)
list_file.pack(side="left", fill="both", expand=True)

scrollbar.config(command=list_file.yview)


#저장 경로 프레임
path_frame = LabelFrame(root, text="저장 경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True,padx=5, pady=5, ipady=4) #fill=x -> 좌우로 쫙 늘리기. #ipady: 엔트리 부분 높이 변경

btn_dest_path = Button(path_frame, text="찾아 보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)


#옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

#1. 가로 넓이 옵션
#1-1. 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로 넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

#1-2. 가로 넓이 콤보
opt_width = ["원본 유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

#2. 간격 옵션
#2-1. 간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

#2-2. 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

#3. 파일 포맷 옵션
#3-1. 파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

#3-2. 파일 포맷 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)


#진행 상황 프레임
frame_progress = LabelFrame(root, text="진행 상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)


#실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, width=12, text="닫기", command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, width=12, text="시작", command=start)
btn_start.pack(side="right", padx=5, pady=5)






root.mainloop() #창 닫히지 않게.