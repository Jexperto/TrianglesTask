class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class LineSegment:
    def __init__(self, p1, p2):
        self.first = p1
        self.second = p2

    def get_bounding_box(self):
        return [Point(min(self.first.x, self.second.x), min(self.first.y, self.second.y)),
                Point(max(self.first.x, self.second.x), max(self.first.y, self.second.y))]


epsilon = 0.0001


def cross_product(a, b):
    res = a.x * b.y - b.x * a.y
    return res


# a - point box b - point box
# Check if bounding boxes do intersect. If one bounding box touches the other, they do intersect.
def do_bounding_boxes_intersect(a, b):
    res = a[0].x <= b[1].x and a[1].x >= b[0].x and a[0].y <= b[1].y and a[1].y >= b[0].y
    return res


# a - line segment b - point
# Checks if a Point is on a line
def is_point_on_line(a, b):
    tempA = LineSegment(Point(0, 0), Point(a.second.x - a.first.x, a.second.y - a.first.y))
    tempB = Point(b.x - a.first.x, b.y - a.first.y)
    r = cross_product(tempA.second, tempB)
    res = abs(r) < epsilon
    return res


# Checks if a point is right of a line. If the point is on the line, it is not right of the line.
# a - line segment, b - point
def is_point_right_of_line(a, b):
    tempA = LineSegment(Point(0, 0), Point(a.second.x - a.first.x, a.second.y - a.first.y))
    tempB = Point(b.x - a.first.x, b.y - a.first.y)
    r = cross_product(tempA.second, tempB)
    res = r < 0
    return res


# Check if line segment first touches or crosses the line that is defined by line segment second.
# a,b - line segments
def line_segment_touches_or_crosses_line(a, b):
    res = is_point_on_line(a, b.first) or is_point_on_line(a, b.second) or (
            is_point_right_of_line(a, b.first) ^ is_point_right_of_line(a, b.second))
    return res


# Check if line segments intersect
# a,b - line segments
def do_lines_intersect(a, b):
    box1 = a.get_bounding_box()
    box2 = b.get_bounding_box()
    res = do_bounding_boxes_intersect(box1, box2) and line_segment_touches_or_crosses_line(a,
                                                                                           b) and line_segment_touches_or_crosses_line(
        b, a)
    return res


def get_line_intersection(line1, line2):
    end1 = Point(line1.second.x - line1.first.x, line1.second.y - line1.first.y)
    end2 = Point(line2.second.x - line2.first.x, line2.second.y - line2.first.y)
    denom = end1.x * end2.y - end2.x * end1.y
    if denom == 0:
        return 0
    denomPositive = denom > 0
    s_numer = (end1.x * (line1.first.y - line2.first.y) - end1.y * (line1.first.x - line2.first.x))
    t_numer = (end2.x * (line1.first.y - line2.first.y) - end2.y * (line1.first.x - line2.first.y))
    # Collision detected
    t = t_numer / denom
    s = s_numer / denom

    intersection = Point(line1.first.x + (t * end1.x), line1.first.y + (t * end1.y))
    return intersection


def get_line_intersection(a, b):
    # y = k1*x+b1
    # y = k2*x+b2
    # k1*x + b1 = k2*x + b2
    # (k1-k2)*x = k2 - k1
    # x = (k2 - k1)/(k1-k2)
    k1 = (a.first.y - a.second.y) / (a.first.x - a.second.x)
    k2 = (b.first.y - b.second.y) / (b.first.x - b.second.x)
    b1 = a.first.y - k1 * a.first.x
    b2 = b.first.y - k2 * b.first.x
    x1 = (b2 - b1) / (k1 - k2)
    y1 = k1 * x1 + b1
    return Point(x1, y1)
