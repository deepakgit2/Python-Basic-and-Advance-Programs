# It is the implementation of Towe of Henoi Problem
# You can see animation when you run into terminal
# Implemented --python-version 3.7

import os, time

n = 5
clear = 'cls' if os.sys.platform == 'win32' else 'clear'
# Initializing towers
A, B, C = list(range(1,n+1)), [], []

# To see all three tower
def show(arr, frm, to):
	gap = 20
	print (' '*gap,'A  B  C')
	for c in range(n):
		print (' '*gap, end=' ')
		for r in range(3):
			print (arr[r][c],' ', end='')
		print ('\n')
	print ( 'Move a disk from tower {} to {}'.format(frm, to) )
	time.sleep(.5)

# Move one disk from one tower to another tower
def move(frm, to):
	global A,B,C
	exec('t = {}.pop(0)'.format(frm))
	exec('{}.insert(0,t)'.format(to))

	arr = [[0]*(n-len(A))+A, [0]*(n-len(B))+B, [0]*(n-len(C))+C]
	os.system(clear)
	show(arr, frm, to)
	
# Recursive Function
def TOH(n, frm, to, empty):
	if n == 1:
		move(frm, to)
	else:
		TOH(n-1, frm, empty, to)
		TOH(1, frm, to, empty)
		TOH(n-1, empty, to, frm)	

TOH(n, 'A', 'B', 'C')
