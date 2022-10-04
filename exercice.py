#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	liste = []
	for i in range(len(numbers)):
		liste.append(max(numbers[i]))
	return liste


def join_integers(numbers):
	return int("".join([str(i) for i in numbers]))


def generate_prime_numbers(limit):
	liste = []
	for nombre in range(2, limit+1):
		for i in range(2, nombre):
			if nombre % i == 0:
				break
		else:
			liste.append(nombre)
	return liste


def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	# liste = []
	if excluded_multiples == None:
		excluded_multiples = 1
	# for i in range(1, num_combinations+1, excluded_multiples):
		# for j in strings:
			# liste.append(j + str(i))   # comprehension de liste moins propre dans ce cas.
	liste = [j + str(i) for i in range(1, num_combinations + 1, excluded_multiples) for j in strings]
	return liste


if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
