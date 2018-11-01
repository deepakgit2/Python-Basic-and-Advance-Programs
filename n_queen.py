# This program is solution of n-queen problem
# problem : n-queen should be arange on n*n chess board in such a way that
#           They should not attack each other
# Output : output will be in n*n matrix where 1 will denote queen and 0 will denote empty place

import numpy as np

n = 10
board = np.zeros((n,n), dtype = int)

def bktrk_gen(a):
	for i in range(1, 1+len(a)):
		if a[-i][1] > 0:
			if a[-i][1] == a[-i][0]:
				a[-i][0] = 0
			else:
				a[-i][0] += 1
				return a, len(a)-i

def position(board, val, i, j):
	alt_pos = []
	for p in range(n):
		if not board[i][p]:
			alt_pos.append([i,p])
			board[i][p] = val
	if not alt_pos:
		return (board, alt_pos)
	for p in range(n):
		if not board[p][j]:
			board[p][j] = val
			
		if i+p < n and j+p < n:
			if not board[i+p][j+p]:
				board[i+p][j+p] = val
				
		if i+p < n and j-p >= 0:
			if not board[i+p][j-p]:
				board[i+p][j-p] = val
				
	return (board, alt_pos)

def init_list(board, x_1, y_1):
	i_list = []
	for x in range(x_1, n):
		for y in range(n):
			if x == x_1:
				y = y_1
			if not board[x][y]:
				board, alt_pos = position(board, x+1, x, y)
				# print board
				i_list.append(alt_pos)
				break
		else:
			return board, i_list
	return board, i_list

t_board, i_list = init_list(board, 0, 0)
col_list = [[0, len(i)-1] for i in i_list]

def arange(board, arr, col, c_elt):
	i_list = []
	c_list = []
	
	for l in range(c_elt+1):
		board, alt_pos = position(board, l+1, arr[l][col[l][0]][0], arr[l][col[l][0]][1])
		
		if alt_pos:
			i_list.append(alt_pos)
			if l <= c_elt:
				c_list.append([col[l][0], len(alt_pos)-1])
			else:
				c_list.append([0, len(alt_pos)-1])

	for x in range(c_elt+1, n):
		for y in range(n):
			if not board[x][y]:
				board, alt_pos = position(board, x+1, x, y)
				# print board
				if alt_pos:
					i_list.append(alt_pos)
					c_list.append([0, len(alt_pos)-1])
				break
		else:
			return board, i_list, c_list

	return board, i_list, c_list

while len(i_list) != n:
	board = np.zeros((n,n), dtype = int)
	col_list, c_elt = bktrk_gen(col_list)
	board, i_list, col_list = arange(board, i_list, col_list, c_elt)

# print board
f_board = np.zeros((n, n), dtype=int)
for i in range(n):
	f_board[i][i_list[i][col_list[i][0]][1]] = 1

print (f_board)