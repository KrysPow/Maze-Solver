from window_class import Window, Point, Line, Cell


def main():
    win = Window(800, 600)
    # line1 = Line(Point(700,0), Point(0, 50))
    # win.draw_line(line1, 'blue')
    cell1 = Cell(200, 300, 400, 500, win)
    cell2 = Cell(100, 200, 300, 400, win, htw=False)
    cell3 = Cell(300.1, 400, 300, 200, win, htw=False, hbw=False)
    #cell4 = Cell(50, 500, 300, 520, win, hbw=False, hlw=False)
    cell1.draw()
    cell2.draw()
    cell3.draw()
    #cell4.draw()
    cell1.draw_move(cell2)
    cell2.draw_move(cell3, undo=True)
    win.wait_for_close()

main()