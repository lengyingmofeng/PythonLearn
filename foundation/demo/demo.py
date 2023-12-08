from tkinter import *
from tkinter import messagebox


def closeallwindow():   # 关闭窗口
    window.destroy()


def closeWindow():   # 弹出对话框
    messagebox.showinfo(title="警告", message="关不掉吧，气不气")
    return


def love():     # 弹出love的对话框
    love = Toplevel(window)
    love.geometry("300x150+610+260")

    label = Label(love, text="男的发订单号", font=("华文行楷", 25))   # 对话框里面的文字
    label.pack()
    label = Label(love, text="女的发微信号", font=("华文行楷", 25))   # 对话框里面的文字
    label.pack()

    entry = Entry(love, font=("楷体", 15))    # 回车
    entry.pack()

    btn = Button(love, text="嗯嗯", width=10, height=2, command=closeallwindow) # 确定按钮
    btn.pack()
    love.protocol("WM_DELETE_WINDOW", closeNoLove)
    return


def noLove():   # 如果点击关闭弹出对话框
    no_love = Toplevel(window)
    no_love.geometry("300x100+610+260")
    no_love.title("你确定？")
    label = Label(no_love, text="不给关不掉", font=("华文行楷", 25))
    label.pack()
    btn = Button(no_love, text="好吧", width=10, height=2, command=no_love.destroy)
    btn.pack()
    no_love.protocol("WM_DELETE_WINDOW", closeNoLove)


def closeNoLove():  # 取消失败的对话框
    messagebox.showinfo(title="警告", message="不给我充，你就关不掉")
    noLove()


window = Tk()   # 创建一个主窗口对象
window.title("姑娘别怕，我不是什么好人哦")   # 主窗口标题
window.geometry("400x400+590+230")  # 大小
window.protocol("WM_DELETE_WINDOW", closeWindow)    # 触发函数事件

label1 = Label(window, text="男的劫财，女的劫色",
               font=("华文行楷", 16), fg="red")     # 文本框
label1.grid()   # 网格
label2 = Label(window, text="给我充100Q币", font=("华文行楷", 30))  # 内容
label2.grid(row=1, column=1, sticky=E)  #

photo = PhotoImage(file="../img.png")  # 背景图
imageLable = Label(window, image=photo)  # 背景图窗口
imageLable.grid(row=2, columnspan=2)    # 背景图的位置

btn1 = Button(window, text="好的", width=15, height=2, command=love)  # 按钮
btn1.grid(row=3, column=0, sticky=W)    # 按钮位置

btn2 = Button(window, text="滚犊子", width=15, height=2, command=noLove)  # 同理
btn2.grid(row=3, column=1, sticky=E)

window.mainloop()   #  调用启动窗口