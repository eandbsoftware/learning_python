import tkinter

class MyGui:
    def __init__(self, text):
        self.text = text

    def handler(self):
        print(self.text)

    def makewidgets(self):
        root = tkinter.Tk()
        frame = tkinter.Frame(root)
        frame.pack()

        # Use a bound method as a callback
        button1 = tkinter.Button(frame, text="Button 1", fg='red', command=self.handler)
        button1.pack(side=tkinter.LEFT)
        root.mainloop() 

gui = MyGui('hello jason')
gui.makewidgets()