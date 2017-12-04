from itertools import cycle, starmap

input = ""

def do_work(input, offset):
    input_cycle = cycle(input)
    for i in range(0, offset):
        next(input_cycle)
    output = sum(list(starmap(lambda x, y: int(x) if x == y else 0, zip(input, input_cycle))))
    print(output)

# *
do_work(input, 1)

# **
do_work(input, len(input)//2)
