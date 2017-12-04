input = """"""

# 1 *

diffs = []

for line in input.splitlines():
    smallest = 9999999999999
    largest = 0
    for number in line.split():
        if int(number) < smallest:
            smallest = int(number)
        if int(number) > largest:
            largest = int(number)
    diffs.append(largest-smallest)

print(sum(diffs))

# 2 **

divs = []

for line in input.splitlines():
    for number in line.split():
        for number2 in line.split():
            if int(number) > int(number2) and int(number) % int(number2) == 0:
                divs.append(int(number) / int(number2))
                break

print(sum(divs))
