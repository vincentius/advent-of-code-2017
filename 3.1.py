# Build the grid
from itertools import cycle
import json

input = 0000

grid = {}
coordinate = (0,0)

moves = cycle([(1,0), (0,1), (-1,0), (0,-1)])
current_move = (0,0)
previous_move = (0,0)
next_allowed = True

for address in range(1, input + 1):
    while True:
        temp_coordinate = (coordinate[0] + current_move[0], coordinate[1] + current_move[1])
        if not grid.get(temp_coordinate):
            coordinate = temp_coordinate
            grid[coordinate] = address
            previous_move = current_move
            current_move = next(moves)
            break
        next(moves)
        next(moves)
        next(moves)
        current_move = previous_move

print(abs(coordinate[0]) + abs(coordinate[1]))