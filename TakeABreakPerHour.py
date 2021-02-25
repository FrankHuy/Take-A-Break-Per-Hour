import tkinter
from tkinter import messagebox
import time


def func():
    top = tkinter.Tk()
    top.withdraw()
    top.wm_attributes('-topmost', 1)
    while True:
        time.sleep(60 * 60)
        result = messagebox.askokcancel("温馨提示", "坐了一个小时了！溜达溜达去！")
        if not result:
            break


if __name__ == '__main__':
    func()
