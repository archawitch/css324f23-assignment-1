def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    cap_x, cap_y, cap_z = 8, 5, 3
    # Try to empty one bottle
    if x > 0:
        yield((0, y, z), x)
    if y > 0:
        yield((x, 0, z), y)
    if z > 0:
        yield((x, y, 0), z)
    # Try to fill up one bottle
    if x < cap_x:
        yield((cap_x, y, z), cap_x - x)
    if y < cap_y:
        yield((x, cap_y, z), cap_y - y)
    if z < cap_z:
        yield((x, y, cap_z), cap_z - z)
    # Try to pour from one to another
    # x -> y
    t = cap_y - y
    if x > 0 and t > 0:
        if x > t:
            yield((x-t, cap_y, z), t)
        else:
            yield((0, y+x, z), x)
    # x -> z
    t = cap_z - z
    if x > 0 and t > 0:
        if x > t:
            yield((x-t, y, cap_z), t)
        else:
            yield((0, y, z+x), x)
    # y -> x
    t = cap_x - x
    if y > 0 and t > 0:
        if y > t:
            yield((cap_x, y-t, z), t)
        else:
            yield((x+y, 0, z), y)
    # y -> z
    t = cap_z - z
    if y > 0 and t > 0:
        if y > t:
            yield((x, y-t, cap_z), t)
        else:
            yield((x, 0, z+y), y)
    # z -> x
    t = cap_x - x
    if z > 0 and t > 0:
        if z > t:
            yield((cap_x, y, z-t), t)
        else:
            yield((x+z, y, 0), z)
    # z -> y
    t = cap_y - y
    if z > 0 and t > 0:
        if z > t:
            yield((x, cap_y, z-t), t)
        else:
            yield((x, y+z, 0), z)
    #end
