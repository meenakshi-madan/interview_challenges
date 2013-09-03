from collections import defaultdict
import time

def tictactoe_bot(board):
	#dictionaries / hash tables for faster lookup
	O = {'h': defaultdict(list), 'v':  defaultdict(list) , 'f': set([]), 'b': set([])}
	C = {'h': defaultdict(list), 'v':  defaultdict(list), 'f': set([]), 'b': set([])}
	X = []
	for i in range(3):
		for j in range(3):
			if board[i][j] == 'C':
				C['h'][i].append(j)
				C['v'][j].append(i)
				if i == j : C['f'].add(i)
				elif i == (2-j): C['b'].add(i)
			elif board[i][j] == 'O':
				O['h'][i].append(j)
				O['v'][j].append(i)
				if i == j : O['f'].add(i)
				elif i == (2-j): O['b'].add(i)
			else: X.append((i,j))

	#check if board is full
	if not X:
		print "No space, this board is already full."
		return board
		
	#new game, no moves
	if not O['h'] and not C['h']: #or alternatively if len(X) == 9:
		board[0][0] = 'C'
		return board
	
	#winning situation
	success, board = h_check(board, C)
	if success: return board
	
	success, board = v_check(board, C, O)
	if success: return board
	
	success, board = d_check(board, C, O)
	if success: return board
	
	#block opponent's win
	success, board = h_check(board, O)
	if success: return board
	
	success, board = v_check(board, O, C)
	if success: return board
	
	success, board = v_check(board, O, C)
	if success: return board
	
	#fill first gap available
	if X:
		board[X[0][0]][X[0][1]] = 'C'
		return board
	
	
#horizontal check	
def h_check(board, dic):
	for o in dic['h']:
		if len(dic['h'][o]) == 2 and 'X' in board[o]:
			board[o][board[o].index('X')] = 'C'
			return True, board
	return False, board

#vertical check	
def v_check(board, dic, p):
	for o in dic['v']:
		if len(dic['v'][o]) == 2 and not p['v'].get(o):
			board[[item[o] for item in board].index('X')][o] = 'C'
			return True, board
	return False, board

#diagonal check
def d_check(board, dic, p):
	if len(dic['f']) == 2 and not p['f']:
		x = (set([1,2,3]) - dic['f']).pop()
		board[x][x] = 'C'
		return True, board
		
	if len(dic['b']) == 2 and not p['b']:
		x = (set([1,2,3]) - dic['b']).pop()
		board[x][x] = 'C'
		return True, board
	
	return False, board
	
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