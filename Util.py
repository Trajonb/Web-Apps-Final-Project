# Trajon Brown
# 3/2/21
# testcase: [(9, 2), (2, 7), (1, 8), (4, 3), (5, 1), (7, 4), (8, 6), (3, 5), (6, 9)]
# test output: (((1, 8), (2, 7)), 1.4142135623730951)
import math


P = [(9, 2), (2, 7), (1, 8), (4, 3), (5, 1), (7, 4), (8, 6), (3, 5), (6, 9)]


def find_closest_point(array):
    mi = dist(array[0], array[1])
    p1 = array[0]
    p2 = array[1]
    len_array = len(array)
    if len_array == 2:
        return p1, p2, mi

    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if i != 0 and j != 1:
                distance = dist(array[i], array[j])
                # print(distance)
                if distance <= mi:
                    p1 = array[i]
                    p2 = array[j]
                    mi = distance

    return p1, p2, mi


def qsort(L, coord, first=0, last=None):
    if last is None:
        last = len(L) - 1
    if first < last:
        p = L[first][coord]
        low = first + 1
        mid = last
        while low <= mid:
            while low <= mid and L[low][coord] <= p:
                low += 1
            while low <= mid and L[mid][coord] >= p:
                mid -= 1
            if low <= mid:
                L[low], L[mid] = L[mid], L[low]
        L[first], L[mid] = L[mid], L[first]
        qsort(L, coord, first, mid - 1)
        qsort(L, coord, mid + 1, last)
        return L


def closest_pair(ax, ay):
    ln_ax = len(ax)  # It's quicker to assign variable
    if ln_ax <= 3:
        return find_closest_point(ax)  # A call to bruteforce comparison

    mid = ln_ax // 2  # Division without remainder, need int
    Qx = ax[:mid]  # Two-part split
    Rx = ax[mid:]

    # Determine midpoint on x-axis
    midpoint = ax[mid][0]
    Qy = list()
    Ry = list()
    for x in ay:  # split ay into 2 arrays using midpoint
        if x[0] <= midpoint:
           Qy.append(x)
        else:
           Ry.append(x)

    # Call recursively both arrays after split
    (p1, q1, mi1) = closest_pair(Qx, Qy)
    (p2, q2, mi2) = closest_pair(Rx, Ry)

    # Determine smaller distance between points of 2 arrays
    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)

    # Call function to account for points on the boundary
    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)

    # Determine smallest distance for the array
    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x)  # store length - quicker
    mx_x = p_x[ln_x // 2][0]  # select midpoint on x-sorted array
    # Create a subarray of points not further than delta from
    # midpoint on x-sorted array
    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    best = delta  # assign best value to delta
    ln_y = len(s_y)  # store length of subarray for quickness
    for i in range(ln_y - 1):
        for j in range(i+1, min(i + 7, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best


Px = qsort(P[:], 0)
# print(Px)
Py = qsort(P[:], 1)
# print(Py)
print(closest_pair(Px, Py))
