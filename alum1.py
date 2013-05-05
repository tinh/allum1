#! /usr/bin/env python3.3

import sys, random

def pick_allum(allums, rank):
	while True:
		print('pick a nb of allum (', allums[rank], 'max)', end = ' ')
		nb_allum = int(input())
		if nb_allum <= allums[rank]:
			return nb_allum

def pick_rank(allums, total):
	while True:
		print('pick a rank (', total, 'max)', end = ' ')
		rank = int(input())
		if rank <= len(allums) and allums[rank - 1]:
			return rank - 1

def comp(allums):
	while True:
		rank = random.randint(1, len(allums))
		if allums[rank - 1] > 0:
			break
	nb_allum = random.randint(1, allums[rank - 1])
	print('comp chose to pick', nb_allum, 'on rank', rank)
	allums[rank - 1] -= nb_allum	
	return nb_allum - allums[rank - 1]

def play(allums, player = 1):
	total = len(allums)
	while total > 0:
		print_allum(allums)
		rank = pick_rank(allums, total)
		nb_allum = pick_allum(allums, rank)
		print('you picked', nb_allum, 'on range', rank + 1)
		allums[rank] -= nb_allum
		if comp(allums) <= 0:
			total -= 1
		if allums[rank] == 0:
			total -= 1

def gen_allum(nb_rang = 4):
	nb_allum = 1
	allums = list(range(nb_rang))
	for i in allums:
		allums[i] = nb_allum
		nb_allum += 2
	return allums

def print_allum(allums):
	i = 0
	while i < len(allums):
		print(' ' * (len(allums) - (i + 1)), end = ' ')
		print('|' * allums[i])
		i += 1

def usage():
	print(sys.argv[0], '[1:player vs computer|2:player vs player] [nb_rangs (by default 4)]')

def main():
	if len(sys.argv) < 2:
		usage()
	else:
		if len(sys.argv) > 2:
			allums = gen_allum(int(sys.argv[2]))
		else:
			allums = gen_allum()
		play(allums, int(sys.argv[1]))

if __name__ == "__main__":
	main()