# Build the grid
from itertools import cycle
import json

input = 00000

grid = {}
coordinate = (0,0)

moves = cycle([(1,0), (0,1), (-1,0), (0,-1)])
adjacents = [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1),(1,-1),(-1,1)]
current_move = (0,0)
previous_move = (0,0)
next_allowed = True

while True:
    adjacent_sum = 0
    while True:
        temp_coordinate = (coordinate[0] + current_move[0], coordinate[1] + current_move[1])
        if not grid.get(temp_coordinate):
            coordinate = temp_coordinate
            for adjacent in adjacents:
                cell = (coordinate[0] + adjacent[0], coordinate[1] + adjacent[1])
                if grid.get(cell):
                    adjacent_sum += grid[cell]
            if adjacent_sum == 0:
                adjacent_sum = 1
            grid[coordinate] = adjacent_sum
            previous_move = current_move
            current_move = next(moves)
            break
        next(moves)
        next(moves)
        next(moves)
        current_move = previous_move
    if adjacent_sum > input:
        print(adjacent_sum)
        break
