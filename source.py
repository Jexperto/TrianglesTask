from tkinter import *

from Geometry import *

width = 640
height = 480
center = height // 2
white = (255, 255, 255)
item = 0
fp = Point(0, 0)
sp = Point(0, 0)


def paint(event):
    global fp, sp, item
    coords = Point(event.x, event.y)
    coords1 = Point(event.x + 1, event.y + 1)
    for i in intersections:
        if approx_equals(Point(event.x, event.y), i):
            coords = i
            coords1 = Point(i.x + 1, i.y + 1)
            break
    fp = coords
    sp = coords1
    item = cv.create_line(fp.x, fp.y, sp.x, sp.y, fill="black", width=2)


def update_paint(event):
    global fp, sp, item
    sp.x, sp.y = event.x, event.y
    cv.coords(item, fp.x, fp.y, sp.x, sp.y)
    # print(x1, y1, x2, y2)


def approx_equals(point1, point2):
    if point1.x + 3 > point2.x and point2.x + 3 > point1.x:
        if point1.y + 3 > point2.y and point2.y + 3 > point1.y:
            return True
    return False


def epsilon_equals(point1, point2):
    if point1.x + epsilon > point2.x and point2.x + epsilon > point1.x:
        if point1.y + epsilon > point2.y and point2.y + epsilon > point1.y:
            return True
    return False


def check(event):
    global trinumber
    coords = cv.coords(lines.__len__() - 1)
    this_line = LineSegment(Point(coords[0], coords[1]), Point(coords[2], coords[3]))
    has_collided = False

    for line in lines:  # find intersections with our line segment
        if do_lines_intersect(line, this_line):
            intersection = get_line_intersection(line, this_line)
            if line == lines[0]:
                # print("item = " + str(item))
                if fp.x < intersection.x < sp.x:
                    fp.x = intersection.x
                    fp.y = intersection.y
                    cv.coords(item, fp.x, fp.y, sp.x, sp.y)
                if sp.x < intersection.x < fp.x:
                    sp.x = intersection.x
                    sp.y = intersection.y
                    cv.coords(item, fp.x, fp.y, sp.x, sp.y)
            elif line == lines[1]:
                # print("item = " + str(item))
                if fp.x > intersection.x > sp.x:
                    fp.x = intersection.x
                    fp.y = intersection.y
                    cv.coords(item, fp.x, fp.y, sp.x, sp.y)
                if sp.x > intersection.x > fp.x:
                    sp.x = intersection.x
                    sp.y = intersection.y
                    cv.coords(item, fp.x, fp.y, sp.x, sp.y)
            elif line == lines[2]:
                # print("item = " + str(item))
                if fp.y > intersection.y > sp.y:
                    fp.x = intersection.x
                    fp.y = intersection.y
                    cv.coords(item, fp.x, fp.y, sp.x, sp.y)
                if sp.y > intersection.y > fp.y:
                    sp.x = intersection.x
                    sp.y = intersection.y
                    cv.coords(item, fp.x, fp.y, sp.x, sp.y)
            # print(intersection.x, intersection.y)
            if not intersections.__contains__(intersection):
                intersections.append(intersection)
            if has_collided and not epsilon_equals(intersection, first_collision):  # if its the first occurrence, we can't make a line segment
                segment = LineSegment(first_collision, intersection)  # make a line segment between current and first intersection
                for other_line in lines:  # go through all of the lines and check what intersects with our current intersection
                    if (other_line != line) and do_lines_intersect(other_line, line):
                        if do_lines_intersect(segment, other_line):
                            trinumber += 1

            else:
                has_collided = True
                first_collision = intersection
    lines.append(this_line)
    print("Triangles total: " + str(trinumber))
    # for i in intersections:
    #     print(i.x, i.y)


root = Tk()
cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()
cv.pack(expand=YES, fill=BOTH)
cv.bind("<Button-1>", paint)
cv.bind("<B1-Motion>", update_paint)
cv.bind("<ButtonRelease-1>", check)

A = Point(width / 2, height / 12)
B = Point(width / 5, height * (5 / 6))
C = Point(width * (4 / 5), height * (5 / 6))
cv.create_line(A.x, A.y, B.x, B.y, C.x, C.y, A.x, A.y, fill="black", width=2)
lines = [LineSegment(A, B), LineSegment(A, C), LineSegment(B, C)]
intersections = [A, B, C]
trinumber = 1

root.mainloop()
