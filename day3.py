file = open("day3puzzleinput.txt", "r")
array_of_rucksacks = file.read().split('\n')

# testing

# text = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""
# array_of_rucksacks = text.split('\n')
# # print(array_of_rucksacks)
# print(array_of_rucksacks)

priorities = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities_map = {}

for i in range(len(priorities)):
    priorities_map[priorities[i]] = i

total_priority = 0

for rucksack in array_of_rucksacks:

    half_point = len(rucksack) // 2
    first_half = rucksack[0:half_point]
    second_half = rucksack[half_point:]


    types = {}
    for letter in first_half:
        if letter not in types:
            types[letter] = 1

    for letter in second_half:
        if letter in types:
            total_priority += priorities_map[letter]
            break

print(total_priority)