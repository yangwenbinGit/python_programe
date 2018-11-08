# python的图像界面 GUI
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    # def createWidgets(self):
    #     self.helloLabel = Label(self, text='Hello, world!')
    #     self.helloLabel.pack()
    #     self.quitButton = Button(self, text='Quit', command=self.quit)
    #     self.quitButton.pack()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题
app.master.title('Hello World')
# 主消息循环
app.mainloop()

# 我们再对这个GUI程序改进一下，加入一个文本框，让用户可以输入文本，然后点按钮后，弹出消息对话框
