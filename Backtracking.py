import time
#checks whether queen is safe or not

count = 0

def safe(mx, r, c):

	for i in range(r):
		if mx[i][c] == '1':         # two queens share the same column
			return False

	(i, j) = (r, c)
	while i >= 0 and j >= 0:
		if mx[i][j] == '1':         # two queens share the same diagonal (left to right)
			return False
		i = i - 1
		j = j - 1

	(i, j) = (r, c)
	while i >= 0 and j < len(mx):
		if mx[i][j] == '1':             # two queens share the same diagonal (right to left)
			return False
		i = i - 1
		j = j + 1

	return True


def solution(mx):
	for r in mx:
		print(str(r).replace(',', '').replace('\'', ''))
	print()


def solveNQ(mx, r):

	global count

	if r == len(mx):
		count += 1
		solution(mx)            # print solution if queens are placed successfully
		return

	for i in range(len(mx)):

		# if safe
		if safe(mx, r, i):
			
			mx[r][i] = '1'          # queen on current square

			solveNQ(mx, r + 1)

			mx[r][i] = '0'          # backtrack and remove the queen from the current square

N = 6   #size of chessboard

mx = [['0' for x in range(N)] for y in range(N)]  #keeps track of the positions of queens

start = time.time()
solveNQ(mx, 0)
end = time.time()

print("Number of solutions: ", count)
print("Time taken", round(end-start,3), "seconds")


