import tkinter

from tkinter import *
from tkinter import messagebox


def song():  # 点击要执行的事件
    # print('获取金币5个')
    messagebox.showinfo('300个获取金币5个')  # 弹出对话框

def get1():
    print(e1.get())

def change(label, text):  # label表示label标签，text输入框
    label['text'] = text.get()



try:
    tk = Tk()
    tk.title('studyTK')
    screen_w = tk.winfo_screenwidth()  # 获取屏幕宽度
    screen_h = tk.winfo_screenheight()  # 获取屏幕高度

    print(f'{tk.title} --- {screen_h} --- {screen_w}')

    tk.geometry(f'{screen_w}x{screen_h}')  # x只能是小写 设置窗口大小
    # 设置窗口宽高是否可以改变，True:可以 False：不可以
    # tk.resizable(width=False, height=False)

    # destroy销毁
    butt = Button(tk, text='点击我,关闭', bg='blue', fg='red', activebackground='orange', command=tk.destroy)  # 创建按钮
    butt1 = Button(tk, text='点击我获取金币', command=song)  # 创建按钮
    butt.pack()  # 将组件布局到窗口上
    butt1.pack()
    tk.mainloop()

    # 输入框
    e1 = Entry(tk)
    # e1.pack()
    e1.place(x=100, y=20, width=150, height=35)  # 布局到指定位置
    b1 = Button(tk, text='获取信息', command=get1)  # 获取信息按钮
    b2 = Button(tk, text='退出', command=tk.destroy)  # 退出按钮
    b1.place(x=100, y=60, width=50, height=30)
    b2.place(x=200, y=60, width=50, height=30)

    e1.insert('insert', '请输入你的名字')

    lab1 = Label(tk, text='这是一个label标签', bg='pink')  # 设置标签内容为这是一个label标签，背景颜色为粉色
    lab1.place(x=100, y=100, width=280, height=30)

    e1 = Entry(tk)  # 创建输入框
    e1.place(x=100, y=200, width=280, height=30)
    e1.insert('insert', '清欢')  # 在文本框中插入内容


    but = Button(tk, text='更改标签内容', command=lambda: change(lab1, e1))
    but.place(x=100, y=250, width=100, height=30)




    # 显示
    tk.mainloop()

except Exception as e:
    print(f'{e}')
finally:
    print(f'{1}')



