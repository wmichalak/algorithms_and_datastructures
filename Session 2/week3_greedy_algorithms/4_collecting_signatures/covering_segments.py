# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):

    # initialize
    points = []
    center_points = []
    for s in segments:
        points.append((s.start, s.end))
    points = sorted(points)

    ## define intersection segment with int_l and int_r of first two lines,
    # starting with int_r = first segment r point and int_l second segment l point
    int_l, int_r = points[0]

    # now work through each segment - ask whether it intersects our current segment
    for line in points[1:]:
        if int_r - line[0] >= 0: # There is overlap,
            # set new int_l
            int_l = line[0]
        elif int_r - line[0] < 0:  # There is no overlap
            # Assign point
            center_points += [int_l]

            # set new starting points
            int_l = line[0]
            int_r = line[1]

    # Add final centerpoint
    center_points += [int_l]

    return center_points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
