input = """"""

from itertools import permutations, chain, combinations
# * 
invalid_ctr = 0
valid_ctr = 0

for line in input.splitlines():
    perms = []
    string_list = []
    for word in line.split():
        perms.append(combinations(word, len(word)))

    perms = tuple(chain(*perms))

    if len(perms) > len(set(perms)):
        invalid_ctr += 1
    else:
        valid_ctr += 1

print("*")
print(f"Invalid: {invalid_ctr}")
print(f"Valid: {valid_ctr}")


# **
invalid_ctr = 0
valid_ctr = 0

for line in input.splitlines():
    perms = []
    string_list = []
    for word in line.split():
        perms.append(set(permutations(word)))

    perms = tuple(chain(*perms))

    if len(perms) > len(set(perms)):
        invalid_ctr += 1
    else:
        valid_ctr += 1

print("**")
print(f"Invalid: {invalid_ctr}")
print(f"Valid: {valid_ctr}")