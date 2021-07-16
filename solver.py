

example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]


def find_empty_spaces(maze):
	for row in range(9):
		for column in range(9):
			if maze[row][column] == -1:
				return row,column

	return None,None


def check_if_valid(maze,number,row,column):
	if number in maze[row]:
		return False

	column_ = [maze[i][column] for i in range(9)]
	if number in column_:
		return False

	start = (row//3)*3   
	end  = (column//3)*3 
	
	for i in range(start,start+3):
		for j in range(end,end+3):
			if maze[i][j] == number:
				return False

	return True


def solver(maze):

	row,column = find_empty_spaces(maze)

	if row  is None:
		return True

	for num in range(1,10):
		response = check_if_valid(maze,num,row,column)
		if response:
			maze[row][column] = num
			if solver(maze):
				return True
		
		maze[row][column] = -1

	return False


def solve_for_game():
	solver(example_board)
	return example_board


