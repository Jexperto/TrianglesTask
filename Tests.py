from Geometry import *

width = 640
height = 480
center = height // 2
white = (255, 255, 255)
item = 0
fp = Point(0, 0)
sp = Point(0, 0)


# def paint(event):
#     global fp, sp , item
#     fp.x, fp.y = event.x, event.y
#     sp.x,sp.y = event.x + 1, event.y + 1
#     item = cv.create_line(fp.x, fp.y, sp.x, sp.y, fill="black", width=2)
#
#
# def update_paint(event):
#     global fp, sp , item
#     sp.x, sp.y = event.x, event.y
#     cv.coords(item, fp.x, fp.y, sp.x, sp.y)
#     print(fp.x, fp.y ,sp.x, sp.y)


# root = Tk()
#
# cv = Canvas(root, width=width, height=height, bg='white')
# cv.pack()
#
# cv.pack(expand=YES, fill=BOTH)
# # cv.bind("<Button-1>", paint)
# # cv.bind("<B1-Motion>", update_paint)
def testPointRightOfLine():
    line = LineSegment(Point(0, 0), Point(0, 7))
    a = Point(5, 5);
    return is_point_right_of_line(line, a)  # true


def testPointLeftOfLine():
    line = LineSegment(Point(0, 0), Point(0, 7))
    a = Point(-5, 5)
    return is_point_right_of_line(line, a)  # false


def testPointOnLine1():
    line = LineSegment(Point(0, 0), Point(4, 4))
    a = Point(3, 3);
    return is_point_right_of_line(line, a)  # false


def testPointOnLine():
    line = LineSegment(Point(4, 4), Point(0, 0))
    a = Point(3, 3);
    return is_point_right_of_line(line, a)  # false


def mytest():
    l1 = LineSegment(Point(568, 119), Point(507, 246))
    l2 = LineSegment(Point(532, 398), Point(539, 398))
    print(get_line_intersection(l1, l2).x, get_line_intersection(l1, l2).y)
    return do_lines_intersect(l1, l2)


# print("first x - %s : first y - %s : second x - %s : second y - %s :" %(l1.first.x, l1.first.y, l1.second.x, l1.second.y))
print(testPointLeftOfLine())
print(testPointOnLine1())
print(testPointRightOfLine())
print(mytest())

# root.mainloop()
