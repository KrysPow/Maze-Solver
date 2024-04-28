from window_class import Window, Point, Line, Cell
from maze import Maze


def main():
    win = Window(800, 600)
    # line1 = Line(Point(700,0), Point(0, 50))
    # win.draw_line(line1, 'blue')
 
    num_cols = 12
    num_rows = 10


    m1 = Maze(10, 10, num_rows, num_cols, 50, 50, win, seed=None)
    m1.solve()

    win.wait_for_close()

main()