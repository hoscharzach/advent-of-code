import functools

f = open("adventofcode-day1.txt", "r")
split_by_double_space = f.read().split("\n")

parsed = []
one_elf = []

for i in range(len(split_by_double_space)):
    if i == len(split_by_double_space) - 1 or split_by_double_space[i] == "":
        parsed.append(one_elf)
        one_elf = []
    else:
        one_elf.append(int(split_by_double_space[i]))

most_calories = 0
elf_carrying_most = 0

for i in range(len(parsed)):
    total_cals_for_elf = functools.reduce(lambda a,b: a + b, parsed[i])

    if total_cals_for_elf > most_calories:
        most_calories = total_cals_for_elf
        elf_carrying_most = i

def myKey(x):
    return sum(x)

parsed.sort(key=myKey, reverse=True)

top_three_cals = 0
for elf in parsed[0:3]:
    top_three_cals += sum(elf)
