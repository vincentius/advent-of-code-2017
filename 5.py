# *
inp = """"""

inp = inp.splitlines()
inp = [int(x) for x in inp]
position = 0
step = 0
while True:
    try:
        item = inp[position]
    except Exception:
        break
    step += 1
    inp[position] += 1
    position += item

print(step)

# **
inp = """"""

inp = inp.splitlines()
inp = [int(x) for x in inp]
position = 0
step = 0
while True:
    try:
        item = inp[position]
    except Exception:
        break
    step += 1
    if item > 2:
        inp[position] -= 1
    else:
        inp[position] += 1
    position += item

print(step)