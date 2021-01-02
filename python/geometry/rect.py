import skgeom as sg
import matplotlib.pyplot as plt
from skgeom.draw import draw
from random import random as r
import itertools
import math

def draw_rv():
    segments = []
    for i in range(10):
        segments.append(sg.Segment2(sg.Point2(r(), r()),
                                    sg.Point2(r(), r())))

    intersections = []
    for s1, s2 in itertools.permutations(segments, 2):
        isect = sg.intersection(s1, s2)
        if isect:
            intersections.append(isect)

    for s in segments:
        draw(s)
    for i in intersections:
        draw(i)

    HEIGHT = 10
    THETA_H = 45
    THETA_V = 60
    
    pt_h_r = sg.Point2(HEIGHT * math.tan(THETA_H * math.pi / 180), 0)
    pt_v_r = sg.Point2(HEIGHT * math.tan(THETA_V * math.pi / 180), 0)
    print(dir(sg.Transformation2))
    pt_v_r = pt_v_r.transform(sg.Transformation2.Rotation(3, math.pi/2))
    pt_r = sg.Segment2(pt_h_r, pt_v_r)
    draw(pt_h_r)
    draw(pt_v_r)
    draw(pt_r)
    plt.show()

def calc_rv():
    a = sg.Segment3(sg.Point3(3, 5, 2), sg.Point3(0, -2, 2))
    b = sg.Segment3(sg.Point3(5, 3, 2), sg.Point3(-2, -2, 2))
    v = sg.Ray3(sg.Point3(0, 0, 10), sg.Vector3(0, 0, -2))
    gnd = sg.Plane3(sg.Point3(0, 0, 0), sg.Point3(4, 4, 0), sg.Point3(0, 4, 0))
#     print(dir(v))
    print(v.transform(sg.Transformation3()))
#     print(b.perpendicular(sg.Sign.COUNTERCLOCKWISE))
    i = sg.intersection(gnd, v)
    print(i)


if __name__ == '__main__':
#     calc_rv()
    draw_rv()