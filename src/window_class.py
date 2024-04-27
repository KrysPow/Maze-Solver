from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.wm_title('maze solver')
        self.__canvas = Canvas(self.__root, width=width, height=height, bg='white')
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol('WM_DELETE_WINDOW', self.close)


    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()               


    def close(self):
        self.__running = False