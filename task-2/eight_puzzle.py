import copy


def initial_state():
    return ((7, 2, 4, 5, 0, 6, 8, 3, 1), 1, 1)


def is_goal(s):
    return s[0] == (1, 2, 3, 4, 5, 6, 7, 8, 0)


def successors(s):
    _, r, c = s
    new_r, new_c = r-1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r+1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c-1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c+1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1


def is_valid(r, c):
    return 0 <= r <= 2 and 0 <= c <= 2


def move_blank(s, new_r, new_c):
    board, r, c = s
    new_board = list(board)
    new_board[r*3 + c] = new_board[new_r*3 + new_c]
    new_board[new_r*3 + new_c] = 0
    return (tuple(new_board), new_r, new_c)

def h1(s):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    res = 0
    # The for loop counts the number of elements that is different from
    # the goal configuration.
    # We start from index 1 to 8 because the blank is excluded.
    for idx in range(0, 8):
        if goal[idx] != board[idx]:
            res += 1
    return res

def h3(s):
    # implement this function
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    res = 0
    for idx, tile in enumerate(board):
        if(tile > 0):
            # Get index of the goal state
            goal_location = goal.index(tile)
            # Find locations of current tile and its goal tile
            row_board, col_board = idx//3, idx%3
            row_goal, col_goal = goal_location//3, goal_location%3
            # Check if current location and its goal location are not in the same row or column
            if(row_board != row_goal):   res+=1
            if(col_board != col_goal):   res+=1
    return res
