'''Create an n x n matrix and fill it with integers from 1 to n*n in a spiral order, 
starting from the top-left corner and moving to the right initially.'''


# check if next element is inside matrix and is None (hasn't been visited)
def is_valid(size, curr_row, curr_col, matrix):
    return 0 <= curr_row < size and 0 <= curr_col < size and matrix[curr_row][curr_col] is None


size = int(input())
matrix = [[None] * size for _ in range(size)]

# possible directions directions
LEFT, DOWN, RIGHT, UP = 1, 2, 3, 4

directions = {
    RIGHT: (0, 1),
    DOWN: (1, 0),
    LEFT: (0,-1),
    UP: (-1, 0)
}

direction,count = LEFT, 1
row, col = 0, 0

while count <= size ** 2:
    matrix[row][col] = count

    next_row = row + directions[direction][0]
    next_col = col + directions[direction][1]

    if is_valid(size, next_row, next_col, matrix):
        row = next_row
        col = next_col
    else:
        direction += 1
        if direction > 4:
            direction = 1
        row += directions[direction][0]
        col += directions[direction][1]

    count += 1


for row in matrix:
    print(*row)
