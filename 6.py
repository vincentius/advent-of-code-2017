from itertools import cycle

# *

def redistribute(curr_bank, banks):    
    max_value = max(curr_bank)
    max_idx = [i for i,v in enumerate(curr_bank) if v == max_value][0]

    result = list(curr_bank)
    result[max_idx] = 0
    started = False
    for i,x in cycle(enumerate(curr_bank)):
        if i > max_idx or max_idx == len(curr_bank) - 1:
            started = True
        if started:
            result[i] += 1
            max_value -= 1
        if max_value == 0:
            break
    return tuple(result)

curr_bank = "" # input goes here

curr_bank = tuple([int(i) for i in curr_bank.split()])
banks = []

while curr_bank not in banks:
    banks.append(curr_bank)
    curr_bank = redistribute(curr_bank, banks)

print(len(banks))

# **

first_occ = [i for i,v in enumerate(banks) if v == curr_bank][0]
print(len(banks) - first_occ)