# N-Queen problem solution
# Implemented --python-version 3.7

# n*n Board size (must be >= 4)
n = 8

arr = [-1 for _ in range(n)]

def available_space(row, col):
	for idx in range(col):
		# Check row wise attack
		if arr[idx] == row:
			return False
		# Check diagonally attack (main diagonal)
		if arr[idx] - row + col - idx == 0:
			return False
		# Check diagonally attack (second diagonal)
		if arr[idx] - row == col - idx:
			return False
	return True

col = 0
# Backtracking...
while col < n:
	for row in range(arr[col]+1, n):
		if available_space(row, col):
			arr[col] = row
			col += 1
			break
	else:
		for idx in range(col, n):
			arr[idx] = -1
		col -= 1
# output will be position (0 to n-1) of queen in that column
print(arr)
