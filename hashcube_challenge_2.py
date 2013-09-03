#sums = [sumOfColumn1, sumOfColumn2, sumOfColumn3, sumOfRow1, sumOfRow2, sumOfRow3, sumOfDiagFront, sumOfDiagBack]
from collections import defaultdict
from itertools import chain
import time

def tictactoe_bot(board):
	board_num = [[5 if x == 'C' else 3 if x == 'O' else 0 for x in row] for row in board]
	sums = [sum(x) for x in zip(*board_num)] + [sum(x) for x in board_num] + [sum([board_num[i][i] for i in range(3)]), sum([board_num[i][2-i] for i in range(3)])]

	#empty board
	if sum(sums) == 0:
		board[0][0] = 'C'
		return board
		
	#wining situation
	if 10 in sums:
		x = sums.index(10)
		if x < 3:
			board[[item[x] for item in board].index('X')][x] = 'C'
			return board
		elif x < 6:
			board[x%3][board[x%3].index('X')] = 'C'
			return board
		elif x == 6:
			for i in xrange(3):
				if board[i][i] == 'X':
					board[i][i] = 'C'
					return board
		else:
			for i in xrange(3):
				if board[i][2-i] == 'X':
					board[i][2-i] = 'C'
					return board
				
	#block opponent's win
	if 6 in sums:
		x = sums.index(6)
		if x < 3:
			board[[item[x] for item in board].index('X')][x] = 'C'
			return board
		elif x < 6:
			board[x%3][board[x%3].index('X')] = 'C'
			return board
		elif x == 6:
			for i in xrange(3):
				if board[i][i] == 'X':
					board[i][i] = 'C'
					return board
		else:
			for i in xrange(3):
				if board[i][2-i] == 'X':
					board[i][2-i] = 'C'
					return board
					
	#fill available spot
	try:
		z = list(chain(*board)).index('X')
		board[z/3][z%3] = 'C'
	except:
		print "Board is full"
	return board


def getBoard():
	print "Enter current tic tac toe board line by line"
	board = []
	for i in range(3):
		board.append(list(raw_input()))
	return board
		

b = getBoard()		
s = time.time()
outpt = tictactoe_bot(b)
print "\n\nOUTPUT:"
for row in outpt:
	print ''.join(row)
	
print time.time() - s