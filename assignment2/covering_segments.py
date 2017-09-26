# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):

    # sort segments
    sorted_segments = []
    while len(segments) != 0: 
        sorted_segments.append(min(segments))
        segments.remove(min(segments))
        
    points = []
    seg = []
    
    # store start/end from first segment    
    seg.append([sorted_segments[0].start, sorted_segments[0].end])
    
    for s in sorted_segments[1:]:
        changed_seg = False
        for i in seg: 
            # if they overlap
            if s.end >= i[0] and s.end <= i[1]:
                i[1] = s.end
                changed_seg = True
            elif s.start >= i[0] and s.start <= i[1]:
                i[0] = s.start
                changed_seg = True
                
        # none of them overlap 
        if not changed_seg: 
            seg.append([s.start, s.end])

    # add points in the point list
    for i in seg:
        points.append(i[1])
            
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end= ' ')
