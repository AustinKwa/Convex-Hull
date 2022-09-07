#  File: Hull.py

#  Description: Returns the convex hull for a set of coordinates

#  Student Name: Austin Kwa

#  Student UT EID: ak38754

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 2/16/2022

#  Date Last Modified: 2/16/2022

import sys

import math

class Point (object):
    # constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y < other.y)
        return (self.x < other.x)

    def __le__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y > other.y)
        return (self.x > other.x)

    def __ge__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y >= other.y)
        return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
    return q.x*r.y + p.x*q.y + p.y*r.x - q.y*r.x - p.x*r.y - p.y*q.x

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
    upper_hull = [sorted_points[0], sorted_points[1]]
    for i in range(2, len(sorted_points)):
        upper_hull.append(sorted_points[i])
        while (len(upper_hull) >= 3) and (det(upper_hull[len(upper_hull) - 3], upper_hull[len(upper_hull) - 2], upper_hull[len(upper_hull) - 1]) > 0):
            del upper_hull[len(upper_hull) - 2]
    
    sorted_points.reverse()
    lower_hull = [sorted_points[0], sorted_points[1]]
    for i in range(2, len(sorted_points)):
        lower_hull.append(sorted_points[i])
        while (len(lower_hull) >= 3) and (det(lower_hull[len(lower_hull) - 3], lower_hull[len(lower_hull) - 2], lower_hull[len(lower_hull) - 1]) > 0):
            del lower_hull[len(lower_hull) - 2]

    del lower_hull[0]
    del lower_hull[len(lower_hull) - 1]

    convex_hull = upper_hull
    for i in lower_hull:
        convex_hull.append(i)

    return convex_hull

# Input: convex_poly is a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
    sum = 0
    for i in range(len(convex_poly) - 1):
        sum += convex_poly[i].x * convex_poly[i + 1].y - convex_poly[i + 1].x * convex_poly[i].y
    
    sum += convex_poly[len(convex_poly) - 1].x * convex_poly[0].y - convex_poly[0].x * convex_poly[len(convex_poly) - 1].y
    return 0.5 * math.fabs(sum)

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    # write your own test cases

    return "all test cases passed"

def main():
    # create an empty list of Point objects
    points_list = []

    # read number of points
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int (line)

    # read data from standard input
    for i in range (num_points):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        x = int (line[0])
        y = int (line[1])
        points_list.append (Point (x, y))

    # sort the list according to x-coordinates
    sorted_points = sorted (points_list)

    '''
    # print the sorted list of Point objects
    for p in sorted_points:
        print (str(p))
    '''

    # get the convex hull
    convex = convex_hull(sorted_points)

    # run your test cases

    # print your results to standard output
    print('Convex Hull')
    
    # print the convex hull
    for p in convex:
        print(str(p))

    # get the area of the convex hull
    area = area_poly(convex)

    # print the area of the convex hull
    print('\nArea of Convex Hull = ' + format(area, '.1f'))

if __name__ == "__main__":
  main()