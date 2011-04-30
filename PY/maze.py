class Maze:
	UP = 1
	RIGHT = 2
	DOWN = 4
	LEFT = 8

	def _init_(self,rows,columns):
		self.grid = []
		for i in range(rows*columns):
			self.grid.append(UP | RIGHT | DOWN | LEFT)
		self.rs = rows
		self.cs = columns

	def random_maze(self,rows,cols):
		ran_maze = Maze(rows,cols)

		walls = []
		for r in range(rows):
			for c in range(cols):
				if r > 0:
					walls.append(Wall(r*cols+c, UP))
				if c > 0:
					walls.append(Wall(r*cols+c, LEFT))
	
		dise = DisjointSet(rows*cols)
		while dise.size > 1:
			random.seed(None)
			walli = random.randint(0,ran_maze.size)
			cell1 = walls[walli].cell
			cell2 = if walls[walli].direction == UP:
						cell1 - cols
						cell1 - 1

			if(dise.find(cell1) != dise.find(cell2)):
				if(walls[walli].direction == UP):
					ran_maze.grid[cell1] ^= UP
					ran_maze.grid[cell2] ^= DOWN
				else:
					ran_maze.grid[cell1] ^= LEFT
					ran_maze.grid[cell1] ^= RIGHT
				dise.join(cell1, cell2)
			walls.pop(walli)
			
		return ran_maze
		
