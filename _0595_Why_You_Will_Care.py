import sys
from tkinter import Button, mainloop
x = Button(
    text='Press me',
    command=lambda: sys.stdout.write('Hello Jason\n')
)
x.pack()
mainloop()