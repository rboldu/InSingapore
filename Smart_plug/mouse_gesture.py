from math import sqrt
from sys import maxsize

_MIN_SEG_LEN = 60

DOWN = 2
LEFT = 4
RIGHT = 6
UP = 8
_strokesStrings = {1:'DL', 2:'D', 3:'DR', 4:'L', 6:'R', 7:'UL', 8:'U', 9:'UR'}

def getGesture(points):
    # Returns a gesture as a list of directional integers, i.e. [2,6,4] for
    # the down-left-right gesture.
    #
    # The points param is a list of tuples of XY points that make up the user's
    # mouse gesture.
    return _identifyStrokes(points)[0]



def getGestureStr(strokes):
    # Returns a string of space-delimited text characters that represent the
    # strokes passed in. For example, getGesture([2, 6, 4]) returns "D R L".
    #
    # The strokes parameter is a list of directional integers, like the kind
    # returned by getGesture().
    if len(strokes) and type(strokes[0]) == type(0):
        # points is a list of directional integers, returned from getGesture()
        return ' '.join(_strokesStrings[x] for x in strokes)
    else:
        # points is returned from getGestureAndSegments()
        return ' '.join(_strokesStrings[x] for x in _identifyStrokes(strokes)[0])

def findClosestMatchingGesture(strokes, gestureList, tolerance=maxsize):
    # Returns the gesture in gestureList that closest matches the gesture in
    # strokes. The tolerance is how many differences there can be and still
    # be considered a match.
    if len(gestureList) == 0:
        return None

    strokes = ''.join(strokes)
    gestureList = [''.join(x) for x in gestureList]
    gestureList = list(frozenset(gestureList)) # make a unique list
    distances = {}
    for g in gestureList:
        dist = levenshteinDistance(strokes, g)
        if dist in distances:
            distances[dist].append(g)
        else:
            distances[dist] = [g]
    smallestKey = min(distances.keys())
    if len(distances[smallestKey]) == 1 and smallestKey <= tolerance:
        return [int(x) for x in distances[min(distances.keys())]]
    else:
        return None

def levenshteinDistance(s1, s2):
    # Returns the Levenshtein Distance between two strings as an integer.

    # http://en.wikipedia.org/wiki/Levenshtein_distance
    # The Levenshtein Distance (aka edit distance) is how many changes (i.e.
    # insertions, deletions, substitutions) have to be made to convert one
    # string into another.
    #
    # For example, the Levenshtein distance between "kitten" and "sitting" is
    # 3, since the following three edits change one into the other, and there
    # is no way to do it with fewer than three edits:
    #   kitten -> sitten -> sittin -> sitting
    len1 = len(s1)
    len2 = len(s2)

    matrix = list(range(len1 + 1)) * (len2 + 1)
    for i in range(len2 + 1):
        matrix[i] = list(range(i, i + len1 + 1))
    for i in range(len2):
        for j in range(len1):
            if s1[j] == s2[i]:
                matrix[i+1][j+1] = min(matrix[i+1][j] + 1, matrix[i][j+1] + 1, matrix[i][j])
            else:
                matrix[i+1][j+1] = min(matrix[i+1][j] + 1, matrix[i][j+1] + 1, matrix[i][j] + 1)
    return matrix[len2][len1]

def setMinStrokeLen(val):
    # Set the length (in pixels) a stroke must be to be recognized as a stroke.
    _MIN_SEG_LEN = val

def getMinStrokeLen():
    # Get the minimum segment length.
    return _MIN_SEG_LEN




# Private Functions:

def _identifyStrokes(points):
    strokes = []
    strokeSegments = []

    # calculate lengths between each sequential points
    distances = []
    for i in range(len(points)-1):
        distances.append( _distance(points[i], points[i+1]) )

    # keeps getting points until we go past the min. segment length
    #startSegPoint = 0
    #while startSegPoint < len(points)-1:
    for startSegPoint in range(len(points)-1):
        segmentDist = 0
        curDir = None
        consistent = True
        direction = None
        for curSegPoint in range(startSegPoint, len(points)-1):
            segmentDist += distances[curSegPoint]
            if segmentDist >= _MIN_SEG_LEN:
                # check if all points are going the same direction.
                for i in range(startSegPoint, curSegPoint):
                    direction = _getDir(points[i], points[i+1])
                    if curDir is None:
                        curDir = direction
                    elif direction != curDir:
                        consistent = False
                        break
                break
        if not consistent:
            continue
        elif (direction is not None and ( (not len(strokes)) or (len(strokes) and strokes[-1] != direction) )):
            strokes.append(direction)
            strokeSegments.append( [startSegPoint, curSegPoint] )
        elif len(strokeSegments):
            # update and lengthen the latest stroke since this stroke is being lengthened.
            strokeSegments[-1][1] = curSegPoint
    return strokes, strokeSegments

def _getDir(coord1, coord2):
    # Return the integer of one of the 8 directions this line is going in.
    # coord1 and coord2 are (x, y) integers coordinates.
    x1, y1 = coord1
    x2, y2 = coord2

    if x1 == x2 and y1 == y2:
        return None # two coordinates are the same.
    elif x1 == x2 and y1 > y2:
        return UP
    elif x1 == x2 and y1 < y2:
        return DOWN
    elif x1 > x2 and y1 == y2:
        return LEFT
    elif x1 < x2 and y1 == y2:
        return RIGHT

    slope = float(y2 - y1) / float(x2 - x1)

    if x2 > x1 and y2 < y1: 
        if slope > -1:
            return RIGHT
        else:
            return UP 
    elif x2 > x1 and y2 > y1:
        if slope > 1:
            return DOWN
        else:
            return RIGHT
    elif x2 < x1 and y2 < y1:
        if slope < 1:
            return LEFT
        else:
            return UP
    elif x2 < x1 and y2 > y1:
        if slope < -1:
            return DOWN
        else:
            return LEFT

def _distance(coord1, coord2):
    # Return distance between two points. This is a basic pythagorean theorem calculation.
    # coord1 and coord2 are (x, y) integers coordinates.
    xdist = coord1[0] - coord2[0]
    ydist = coord1[1] - coord2[1]
    return sqrt(xdist*xdist + ydist*ydist)
