import requests
import pandas

test_group = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg"""

priorities = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities_map = {}

for i in range(len(priorities)):
    priorities_map[priorities[i]] = i

test_group_array = test_group.split("\n")

first_elf_chars = {}
for rucksack in test_group_array:
    for char in rucksack:
        if char not in first_elf_chars:
            first_elf_chars[char] = 1

# print(test_group_array)

# print(dir(requests))
print(dir(pandas))