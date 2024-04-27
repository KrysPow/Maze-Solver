from window_class import Window, Point, Line


def main():
    win = Window(800, 600)
    line1 = Line(Point(700,0), Point(0, 50))
    line2 = Line(Point(50,0), Point(50, 300))
    line3 = Line(Point(0,20), Point(24, 235))
    line4 = Line(Point(32,34), Point(25, 320))
    win.draw_line(line1, 'black')
    win.draw_line(line2, 'red')
    win.draw_line(line3, 'green')
    win.draw_line(line4, 'blue')
    win.wait_for_close()

main()