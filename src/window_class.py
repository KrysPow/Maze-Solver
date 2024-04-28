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


    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)



class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

    
class Cell():
    def __init__(self, x_1, x_2, y_1 , y_2, win=None, hlw=True, hrw=True, htw=True, hbw=True, visited=False):
        self.has_left_wall = hlw
        self.has_right_wall = hrw
        self.has_bottom_wall = hbw
        self.has_top_wall = htw
        self.x_1 = x_1
        self.x_2 = x_2
        self.y_1 = y_1
        self.y_2 = y_2
        self.win = win
        self.visited = visited

    def draw(self):
        if self.has_left_wall:
            self.win.draw_line(Line(Point(self.x_1, self.y_1), Point(self.x_1, self.y_2)), 'black')
        else:
            self.win.draw_line(Line(Point(self.x_1, self.y_1), Point(self.x_1, self.y_2)), 'white')

        if self.has_right_wall:
            self.win.draw_line(Line(Point(self.x_2, self.y_1), Point(self.x_2, self.y_2)), 'black')
        else:
            self.win.draw_line(Line(Point(self.x_2, self.y_1), Point(self.x_2, self.y_2)), 'white')

        if self.has_top_wall:
            self.win.draw_line(Line(Point(self.x_1, self.y_1), Point(self.x_2, self.y_1)), 'black')
        else:
            self.win.draw_line(Line(Point(self.x_1, self.y_1), Point(self.x_2, self.y_1)), 'white')

        if self.has_bottom_wall:
            self.win.draw_line(Line(Point(self.x_1, self.y_2), Point(self.x_2, self.y_2)), 'black')
        else:
            self.win.draw_line(Line(Point(self.x_1, self.y_2), Point(self.x_2, self.y_2)), 'white')

    def draw_move(self, to_cell, undo=False):
        c1 = Point((self.x_2+self.x_1)/2, (self.y_2+self.y_1)/2)
        c2 = Point((to_cell.x_2+to_cell.x_1)/2, (to_cell.y_2+to_cell.y_1)/2)
        line = Line(c1, c2)
        if undo:
            self.win.draw_line(line, 'gray')
        else:
            self.win.draw_line(line, 'red')

        

        


